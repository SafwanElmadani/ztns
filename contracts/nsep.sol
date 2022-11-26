// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

// create an interface for decision point contract
interface Insdp {
    function make_decision(address _address) external view returns(bool);
    }

contract nsep {
    address public address_nsdp; // address of the decision contract

    constructor(address _address_nsdp)
    {
        address_nsdp = _address_nsdp;
    }

//call nsdp function to make a decision
    function permission_to_access(address _address) external view returns(bool)
    {
        return Insdp(address_nsdp).make_decision(_address);
        
    }
    
}
