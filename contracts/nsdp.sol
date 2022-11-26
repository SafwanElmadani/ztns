// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

// all numbers in this contract are multiplied by 10**4 to support decimal numbers precision
// e.g. 5000 => 0.5

contract nsdp {

    struct Entity {
        uint256 id;
        uint256 trust_value;
        bool set;
    }
    uint256 public counter = 0;
    uint256 public threshold = 0;
    mapping(address => Entity) public entities;

    function create_new_entity(address _entity_address, uint256 _trust_value) public 
    {
        //check if the entity is already created
        Entity storage entity_pointer = entities[_entity_address]; //need storage to create a pointer
        require(!entity_pointer.set, "user is already added");
        //store the data
        entities[_entity_address] = Entity(
        {
            id: ++counter,
            //name: "someone",
            trust_value: _trust_value,
            set: true
        }
        );
    }

    //This function gets called from NSEP contract whenever it gets a request to access resources
    function make_decision(address _address) external view returns(bool)
    {
        if (entities[_address].trust_value < threshold)
            {
                return false;
            }
        else
            {
                return true;
            }
    }

    //This function update the threshold value
    function update_threshold(uint256 _threshold) external 
    {
        threshold = _threshold;
    }

    function update_trust_value(address _address, uint256 _trust_value) public
    {
        entities[_address].trust_value = _trust_value;
    }

    function get_trust_value(address _address) public view returns(uint256)
    {
        return entities[_address].trust_value;
    }
        
}
