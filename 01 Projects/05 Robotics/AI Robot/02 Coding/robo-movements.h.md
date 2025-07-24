---
tags:
  - c_lib
  - ai_robot
---

# Robo-Movements.h


here there are 4 situations 

| Situation                                                      | Solution                                                 |
| -------------------------------------------------------------- | -------------------------------------------------------- |
| `current_angle + _positions[id]->_the_angle > SERVO_ANGLE_MAX` | Make the `lhs < SERVO_ANGLE_MAX` ie , limit `_the_angle` |
| `current_angle + _positions[id]->_the_angle < SERVO_ANGLE_MAX` | Make the `lhs > SERVO_ANGLE_MIN` ie , limit `_the_angle` |
|                                                                |                                                          |



```cpp

void Movement::_move(move_position_t* _positions[], uint8_t _num_positions) {
  if(_num_positions < 0 ){
    return;
  }
  else{
    bool _is_all_finished = false;
    while (!_is_all_finished) {
      // go through each position and check if everything is finished
      for (uint8_t i = 0; i < _num_positions; i++) {
        if (_positions[i]->_the_angle = 0){
          _is_all_finished = false;
        }
        else {
          _is_all_finished = true;
        }
      }
      for (uint8_t i = 0; i < _num_positions; i++) {
        // Set the angle of the servo
        
        if (_positions[i]->_the_angle == 0) {
          // If the angle is 0, skip setting the angle
          continue;
        }
        // Check if the servo angle exceeds the maximum angle
        // TODO: Make angle sustainable 
        else if (_positions[i]->_the_angle > 0 && _all_robots[_positions[i]->_id]->get_current_angle() + _positions[i]->_the_angle <= SERVO_ANGLE_MAX ) {
          // move the servo by THE_STEP degrees
          _all_robots[_positions[i]->_id]->set_angle(_all_robots[_positions[i]->_id]->get_current_angle() + THE_STEP);
          // Decrease the angle by THE_STEP
          _positions[i]->_the_angle -= THE_STEP;
          if (_positions[i]->_the_angle < 0) {
            // make it 0 if it goes below 0
            _positions[i]->_the_angle = 0; 
          }
        }
        // else if (_all_robots[_positions[i]->_id]->get_current_angle() + _positions[i]->_the_angle > SERVO_ANGLE_MAX ){
        //   // NOTE: how to limit the angle?
        //   _positions[i]->_the_angle = SERVO_ANGLE_MAX - _all_robots[_positions[i]->_id]->get_current_angle();
        // }
        // else if (_positions[i]->_the_angle < 0 && _all_robots[_positions[i]->_id]->get_current_angle() + _positions[i]->_the_angle >= SERVO_ANGLE_MAX ) {
        //   // If the angle is negative, set the angle to 0
        //   _positions[i]->_the_angle = 0;
        // }
        // else if(_all_robots[_positions[i]->_id]->get_current_angle() + _positions[i]->_the_angle > SERVO_ANGLE_MAX){
        //   // TODO: find what to do here
        // }
      }

      delay(10); // Small delay to allow servo movement
    }
  }

```