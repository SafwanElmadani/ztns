// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;


interface Insep {
    function getString() external view returns (string memory);
    function set_string(string memory _string) external;
    function setAddress(address _address_nsdp) external;
    }

contract nsdp {

    address address_nsep;
    string data;
    constructor(address _address_nsep) {
        address_nsep = _address_nsep;
        data = "hello world 2";
        Insep(address_nsep).setAddress(address(this));
    }

    function call_getstring() external view returns(string memory) {
       // nsep pointer = nsep(address_nsep);
        return Insep(address_nsep).getString();
    }
    function call_setsting(string memory _string) external {
        Insep(address_nsep).set_string(_string);
    }
    function getString() public view returns(string memory) {
        return data;
    }
}
