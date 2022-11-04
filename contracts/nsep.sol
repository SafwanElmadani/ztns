// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

interface Insdp {
    function getString() external view returns (string memory);
    }

contract nsep {
    string someData;
    address public address_nsdp;
    constructor() {
        someData = "hello world 1";

    }
    function setAddress(address _address_nsdp) external{
        address_nsdp = _address_nsdp;
    }

    function getString() public view returns(string memory) {
        return someData;
    }
    function set_string(string memory _string) public {
        someData = _string;
    }

    function call_getstring22() external view returns(string memory) {
        return Insdp(address_nsdp).getString();
    }
    
}
