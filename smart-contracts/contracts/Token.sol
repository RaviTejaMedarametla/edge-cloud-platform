// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract Token {
    string public name = "MyToken";
    string public symbol = "MTK";
    uint256 public totalSupply = 1000000;
    mapping(address => uint256) public balanceOf;

    constructor() {
        balanceOf[msg.sender] = totalSupply;
    }
}
