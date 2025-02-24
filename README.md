# UML Activity Diagrams

## Purpose of Each Diagram

### 1. User Authentication Activity Diagram
The **User Authentication** activity diagram visualizes the login process for users in the RevoBank system. It captures:
- The process of entering login credentials.
- Verification of credentials by the system.
- Handling of incorrect login attempts.
- Successful authentication leading to token generation.
- The final outcome, whether the login succeeds or fails.

### 2. Transaction Handling Activity Diagram
The **Transaction Handling** activity diagram represents the process of handling financial transactions in the RevoBank system. It details:
- How a user initiates a transaction.
- The verification of the account balance before proceeding.
- The transaction process if the balance is sufficient.
- Handling of failed transactions due to insufficient funds.
- The generation of transaction history for successful transactions.

---

## Key Decisions and Processes Represented

### User Authentication:
- **Decision:** Is the entered credential valid?
  - Yes → Generate token and log in.
  - No → Record failed attempt and send an email notification.
- **Process:** 
  - If valid, the system generates a token and grants access.
  - If invalid, the system records the failed login attempt and notifies the user.

### Transaction Handling:
- **Decision:** Does the user have sufficient funds?
  - Yes → Process the transaction and update transaction history.
  - No → Decline the transaction and notify the user.
- **Process:**
  - The user initiates the transaction, and the system verifies account balance.
  - If the balance is sufficient, the transaction is processed and recorded.
  - If insufficient, the transaction fails, and the user is notified.

---

## UML Activity Diagrams
The UML activity diagrams were created using **Lucidchart**:
- **User Authentication:** [Lucidchart Diagram](https://lucid.app/lucidchart/e0641486-acc9-4f04-b759-d0b92dcd568a/edit?viewport_loc=-24%2C-64%2C1730%2C1001%2C0_0&invitationId=inv_41aaa07b-f7cc-44d3-9419-ce6a93b1eeb5)
- **Transaction Handling:** [Lucidchart Diagram](https://lucid.app/lucidchart/afdb94bf-f4ec-40e0-84c1-3ac1ec25fcc0/edit?viewport_loc=420%2C-25%2C1617%2C936%2C0_0&invitationId=inv_4dbfd3cf-634b-4c6f-8cda-576621a6ad42)
