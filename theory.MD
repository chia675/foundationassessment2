1.1) What does SDLC stand for?
SDLC stands for Software Development Life Cycle. It is a process that describes the steps involved in developing 
software. 

1.2) What exception is thrown when divide a number by zero?
ZeroDivisionError

1.3) What is the git command that moves code from the local repository to the remote repository?
git push 

1.4) What does NULL represent in a database?
In a database, a null value represents a missing or unknown value. It is not the same as a zero value. 
A null value is used to indicate that a field does not have a value.

1.5) Name 2 responsibilities of the Scrum Master?
Facilitating Scrum events: The Scrum Master is responsible for facilitating all Scrum events, such as the daily standup, 
sprint planning, sprint review, and sprint retrospective. This includes ensuring that the events are productive and that 
everyone is on the same page.


Removing impediments: The Scrum Master is also responsible for removing impediments to the team's progress. This 
includes things like technical problems, organizational roadblocks, and interpersonal conflicts. The Scrum Master 
helps the team to identify and address these impediments so that they can focus on delivering value.

1.6) Name 2 debugging methods, and when you would use them.
Print debugging: It involves inserting print statements into your code to print out the values of variables and expressions. 
This can help to track down the source of an error by 
seeing what values are being used and where they are coming from. An example of this would be, if you are getting an 
error in a function, you can insert print statements to print out the values of the parameters that are being passed to 
the function. This can help to see if the parameters are being passed correctly.

Debugger: There is a built-in debugger called 'pdb' (Python Debugger) that allows you to step through your code and
inspect variables and their values at each step. One example of this would be, if you need to dive deep into the code,
trace the flow of execution and identify complex issues.

1.7) Looking at the following code, describe a case where this function would throw an error when called.
The function, `can_pay(price, cash_given)`, checks if the `cash_given` amount is greater than or equal to the 
`price`. It returns `True` if the payment can be made and `False` otherwise. However, there is a potential case where 
this function could throw an error when called.

If the `price` or 'cash_given' are non-integers, a TypeError will when trying to perform the comparison operation ('>=').
To handle this, exceptional handling can be used to catch the 'TypeError' and handle it:

def can_pay(price, cash_given):
    try:
        if cash_given >= price:
            return True
        else:
            return False
    except TypeError:
        print("Error: Invalid input. You must enter an integer)



1.8) What is git branching?
Git branching is a core feature of the version control system Git. It allows you to create and manage multiple lines of 
development within a single Git repository. Branching is useful because it enables you to work on different features, 
bug fixes, or experiments in isolation without affecting the main codebase. Each branch can have its own set of commits, 
files, and changes. 

How branching is used in Git:

Creating a branch: You can create a new branch using the `git branch` command. For example, `git branch feature-branch` 
creates a new branch named "feature-branch" based on your current commit.

Switching branches: To switch to a different branch, you can use the `git checkout` command. For example, 
`git checkout feature-branch` switches to the "feature-branch" branch.

Committing changes: Once you're on a branch, you can make changes to files in your working directory and use `git add` 
and `git commit` commands to create commits specific to that branch.

Merging branches: If you're on the "main" branch, running `git merge feature-branch` would merge the 
changes from "feature-branch" into "main".

Resolving conflicts: Git may encounter conflicts when merging branches if changes in the same files 
overlap. In such cases, conflicts will need to be manually resolved before completing the merge.

Branch management: Git provides commands to list, rename, delete, and manage branches. Some common commands include 
`git branch`, `git branch -d`, and `git branch -m` for listing, deleting, and renaming branches, respectively.



1.9) Design a restaurant ordering system.

a. Key Requirements:
1. User Registration: Allow customers to create accounts and store their personal information.
2. Menu Management: Maintain a database of available food and beverage items, including their descriptions, prices, and availability.
3. Order Placement: Enable customers to browse the menu, select items, specify customization options, and add them to their cart.
4. Cart Management: Allow customers to view and modify their cart contents before finalizing the order.
5. Payment Processing: Integrate a secure payment gateway to facilitate online transactions.
6. Order Tracking: Provide customers with real-time updates on the status of their orders.
7. Order Fulfillment: Notify the restaurant staff of incoming orders and facilitate their preparation and delivery.
8. Inventory Management: Track the availability of ingredients or items to ensure that orders can be fulfilled.
9. Customer Feedback: Allow customers to provide feedback and ratings for their orders and overall dining experience.

b. Main Considerations and Problems:
1. User Experience: Designing a user-friendly interface to enhance the ordering process and encourage customer satisfaction.
2. Scalability: Ensuring the system can handle a large number of users and process orders efficiently.
3. Security: Implementing robust security measures to protect user information and secure online payments.
4. Integration: Integrating with external services such as payment gateways and notification systems to provide a seamless experience.
5. Customization: Handling special requests, dietary preferences, and additional options for menu items.
6. Order Prioritization: Determining a strategy to prioritize and manage orders during peak hours.
7. Performance Optimization: Optimizing database queries and system architecture to minimize latency and response time.

c. Potential Components or Tools:
1. Backend Framework: A framework like Flask for building the server-side logic.
2. Database Management: Utilizing a relational database management system like MySQL to store menu items, user information, and order details.
3. Payment Gateway: Integrating a secure and widely-used payment gateway like PayPal to handle online transactions.
4. Real-time Communication: Implementing websockets or a messaging system to facilitate real-time order tracking and notifications.
5. Cloud Infrastructure: Deploying the system on a cloud platform like Amazon Web Services for scalability and reliability.
6. User Interface: Designing a responsive and user-friendly frontend using web technologies like HTML, CSS, and JavaScript.
7. API Integration: Integrating with external services, such as email notification systems, to keep customers and staff informed about order status updates.
8. Analytics and Monitoring: Implementing tools like Google Analytics to gather insights about user behavior and monitor system performance.
