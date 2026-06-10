from dataclasses import dataclass

# ==========================================
# TASK 1: DEFINE MESSAGE STRUCTURES (Data Classes)
# ==========================================

@dataclass
class PerceptionContext:
    """
    Acts as the PerceptionContext.msg file.
    Holds the multi-task probabilities and Rule Space context coming from the AI.
    """
    pedestrian_probability: float
    lead_car_distance: float
    weather_context: str  # e.g., "CLEAR", "WET", "SNOW"
    road_type: str        # e.g., "HIGHWAY", "CITY"


@dataclass
class BehaviorCommand:
    """
    Acts as the BehaviorCommand.msg file.
    Holds the final FSM decision to be sent to the Path Planning controllers.
    """
    behavioral_state: str  # "CRUISING", "ADAPTIVE_FOLLOW", or "EMERGENCY_STOP"
    target_velocity: float # Speed in mph


# ==========================================
# TASK 2: DEVELOP BASE FSM STRUCTURE
# ==========================================

class BehavioralPlanner:
    def __init__(self):
        # Moore Machine State Memory Anchor
        self.current_state = "CRUISING"

    def process_perception(self, context):
        """
        WEEK 2: DUAL-LAYER CONSTRAINED LOGIC ENGINE
        """
        
        # ==========================================
        # LAYER 1: RULE SPACE (Environmental Constraints)
        # ==========================================
        # 1A. Set base baselines assuming CLEAR weather and a HIGHWAY
        max_allowable_speed = 65.0 
        pedestrian_tripwire = 0.75  # Needs 75% AI confidence to hard stop
        safe_follow_distance = 20.0 # Start following at 20 meters

        # 1B. Apply Road Type Constraints
        if context.road_type == "CITY":
            max_allowable_speed = 30.0
            pedestrian_tripwire = 0.60 # Cities have more jaywalkers, be more sensitive!

        # 1C. Apply Weather Constraints (The Multiplier Effect)
        if context.weather_context == "WET":
            max_allowable_speed *= 0.8  # Reduce max speed by 20%
            safe_follow_distance *= 1.5 # Need 50% more braking distance (30 meters)
            pedestrian_tripwire -= 0.10 # Drop threshold (makes it more sensitive)
            
        elif context.weather_context == "SNOW":
            max_allowable_speed *= 0.5  # Cut speed in half
            safe_follow_distance *= 2.0 # Double the braking distance (40 meters)
            pedestrian_tripwire -= 0.20 # Highly sensitive to any pedestrian movement

        # ==========================================
        # LAYER 2: DYNAMIC STATE (FSM Transitions)
        # ==========================================
        # Notice how we no longer use hardcoded numbers here! 
        # We use the dynamically constrained rules from Layer 1.
        
        if context.pedestrian_probability > pedestrian_tripwire:
            self.current_state = "EMERGENCY_STOP"
            
        elif context.lead_car_distance < safe_follow_distance:
            self.current_state = "ADAPTIVE_FOLLOW"
            
        else:
            self.current_state = "CRUISING"

        # ==========================================
        # MOORE MACHINE OUTPUT
        # ==========================================
        if self.current_state == "EMERGENCY_STOP":
            velocity = 0.0
            
        elif self.current_state == "ADAPTIVE_FOLLOW":
            # Match the lead car's speed, BUT use min() to ensure we NEVER 
            # exceed the Rule Space max_allowable_speed!
            velocity = min(context.lead_car_velocity, max_allowable_speed)
            
        else: # CRUISING
            velocity = max_allowable_speed

        # Return the final command (Assuming BehaviorCommand is imported)
        return BehaviorCommand(
            behavioral_state=self.current_state,
            target_velocity=velocity
        )

# ==========================================
# TEST RIG: VERIFYING THE PLUMBING WORKS
# ==========================================
if __name__ == "__main__":
    # Initialize the brain
    planner = BehavioralPlanner()

    # Create a fake scenario: A pedestrian suddenly walks out in clear weather
    mock_sensor_input = PerceptionContext(
        pedestrian_probability=0.85, 
        lead_car_distance=50.0, 
        weather_context="CLEAR", 
        road_type="CITY"
    )

    print("--- Autonomous Vehicle FSM Test ---")
    print(f"Incoming Sensor Data: Pedestrian Prob = {mock_sensor_input.pedestrian_probability}")
    
    # Feed the data into the FSM
    output_command = planner.process_perception(mock_sensor_input)
    
    # Print the result
    print(f"Resulting State: {output_command.behavioral_state}")
    print(f"Resulting Velocity Command: {output_command.target_velocity} mph")