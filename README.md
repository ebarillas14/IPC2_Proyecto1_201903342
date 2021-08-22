#Installation Guide For Virtual Environment and Packages

A Virtual Environment is an environment that allow us to install the packages 
that we use in the project without installing it directly in our machine.

## Creating the Virtual Environment (venv)
1) Run the following command to create the Virtual Environment with name venv
    <ul>
        <li>python -m venv venv</li>
    </ul>
## Installing the Packages in the venv

 1) activate the venv by using this command: <br>
    <ul>
        <li>source venv/bin/activate for Linux or Mac</li>
        <li>venv\Scripts\activate for Windows</li>
    </ul>
 2) run the following command:
    <ul>
        <li>pip install -r requirements</li>
    </ul>