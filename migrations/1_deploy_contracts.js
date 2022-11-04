var nsdp_contract = artifacts.require("nsdp");
var nsep_contract = artifacts.require("nsep");

module.exports = async function(deployer, network, accounts) {
  // deployment steps
    await deployer.deploy(nsep_contract);
    //access information about your deployed contract instance
    let x = await deployer.deploy(nsdp_contract, nsep_contract.address);
    console.log(x);
    const instance_dp = await nsdp_contract.deployed();
    //console.log(instance.address);
    const instance_ep = await nsep_contract.deployed();
//    console.log(instance_ep.address);
//    console.log(nsep_contract.address);
//    instance_ep.setAddress(instance_dp.address);
    
};






//module.exports = function(deployer, network, accounts) {
  // deployment steps
  //  console.log(accounts);
  //  deployer.deploy(nsdp_contract, accounts[0]);
  //  deployer.deploy(nsep_contract);
// };
