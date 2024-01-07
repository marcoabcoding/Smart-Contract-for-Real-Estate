class RealEstateContract:
    """
    A simplified smart contract for real estate transactions.
    Manages the process between a buyer and a seller for property transfer.
    """
    def __init__(self):
        # Initialize the contract with default values
        self.buyer = None
        self.seller = None
        self.property_details = {}
        self.price = 0
        self.buyer_paid = False
        self.property_transferred = False

    def initiate_contract(self, buyer, seller, property_details, price):
        # Set up the contract with buyer, seller, property details, and price
        if not self.buyer and not self.seller:
            self.buyer = buyer
            self.seller = seller
            self.property_details = property_details
            self.price = price
            return "Contract initiated!"
        return "Contract is already in place."

    def verify_ownership(self, current_owner):
        # Mock function to verify property ownership
        # In real-world scenarios, this would involve complex legal and public record checks
        return current_owner == self.seller

    def pay(self, buyer, amount):
        # Handle payment from the buyer
        if buyer == self.buyer and amount == self.price and not self.buyer_paid:
            self.buyer_paid = True
            return "Payment received."
        return "Payment failed."

    def transfer_property(self):
        # Confirm the transfer of property if payment is made and ownership is verified
        if self.buyer_paid and self.verify_ownership(self.seller):
            self.property_transferred = True
            return "Property transferred."
        return "Payment not received or ownership verification failed. Cannot transfer property."

    def finalize_transaction(self):
        # Finalize the transaction after confirming payment and property transfer
        if self.buyer_paid and self.property_transferred:
            return f"Transaction finalized. {self.price} transferred to {self.seller}."
        return "Transaction cannot be finalized yet."

    def contract_status(self):
        # Return the current status of the contract
        return {
            "buyer": self.buyer,
            "seller": self.seller,
            "property_details": self.property_details,
            "price": self.price,
            "buyer_paid": self.buyer_paid,
            "property_transferred": self.property_transferred
        }

# Example usage
property_details = {
    "address": "123 Main St",
    "type": "House",
    "bedrooms": 3,
    "bathrooms": 2
}

contract = RealEstateContract()
print(contract.initiate_contract("Alice", "Bob", property_details, 500000))  # Initiate the contract
print(contract.pay("Alice", 500000))                                        # Alice makes payment
print(contract.transfer_property())                                         # Transfer property
print(contract.finalize_transaction())                                      # Finalize transaction
