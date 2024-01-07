# Description

The RealEstateContract class in the script models a transaction between a buyer and a seller for the purchase of a property. It manages the process including contract initiation, payment, property transfer, and finalization of the transaction.
Features

    Contract initiation with specific buyer, seller, property details, and price.
    Payment processing from the buyer.
    Property transfer upon payment and ownership verification.
    Transaction finalization after successful property transfer.
    Contract status tracking.

# Code Structure

    __init__: Initializes the contract with default values.
    initiate_contract: Starts the contract with buyer, seller, property details, and price.
    verify_ownership: Mock function to verify property ownership.
    pay: Manages the payment from the buyer.
    transfer_property: Ensures property transfer after payment and ownership verification.
    finalize_transaction: Completes the transaction once all conditions are met.
    contract_status: Shows the current state of the contract.

# Usage

To use the script, create an instance of the RealEstateContract class and invoke its methods to simulate a real estate transaction.
