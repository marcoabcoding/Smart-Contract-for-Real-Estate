
## Overview
This repository contains a Python script simulating a basic smart contract for e-commerce transactions. Designed to demonstrate the fundamental concept of a smart contract between a buyer and a seller in an e-commerce setting.

## Description
The `SmartContract` class in the script represents a basic model of a smart contract. It facilitates a transaction between a buyer and a seller for a specified product at a set price. The contract ensures that the item is delivered only after the payment is confirmed.

### Features
- Initiation of a contract with buyer, seller, and price details.
- Handling of payment from the buyer.
- Validation of payment before allowing item delivery.
- Finalizing the transaction after delivery.
- Tracking the current status of the contract.

### Code Explanation
- `initiate_contract`: Sets up the contract with the buyer, seller, and price.
- `pay`: Simulates the payment process by the buyer.
- `deliver_item`: Checks if the payment is made before marking the item as delivered.
- `finalize_transaction`: Finalizes the transaction after confirming payment and delivery.
- `contract_status`: Provides the current status of the contract.

## Usage Example
```python
contract = SmartContract()
print(contract.initiate_contract("Alice", "Bob", 100))
print(contract.pay("Alice", 100))
print(contract.deliver_item())
print(contract.finalize_transaction())
