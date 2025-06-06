const { expect } = require('chai');

describe('Token', function () {
  it('Deployment should assign the total supply of tokens to the owner', async function () {
    const [owner] = await ethers.getSigners();
    const Token = await ethers.getContractFactory('Token');
    const token = await Token.deploy();
    await token.deployed();
    const ownerBalance = await token.balanceOf(owner.address);
    expect(await token.totalSupply()).to.equal(ownerBalance);
  });
});
