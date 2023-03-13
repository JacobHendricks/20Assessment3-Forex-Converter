### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?  
  Python is used for backend and talking to databases.  JavaScript is run in the browser and used to modify HTML.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming crashing.  
  dict["c"]

- What is a unit test?  
  Testing one function or method.  Doesn't test integration of components.

- What is an integration test?  
  Testing that components work together, such as "does this route return the right HTML?" or redirects after POST

- What is the role of web application framework, like Flask?  
  To handle web requests, forms, cookies.  Connect to databases and produce dynamic HTML

- You can pass information to Flask either as a parameter in a route URL (like '/foods/pretzel') or using a URL query param (like 'foods?type=pretzel'). How might you choose which one is a better fit for an application?  
  Query param is used when information is coming from a form, or when the user searches for something.  Route URL is more like the subject of a page.

- How do you collect data from a URL placeholder parameter using Flask?  
  <variable_name> in @app.route

- How do you collect data from the query string using Flask?  
  request.args.get("data")

- How do you collect data from the body of the request using Flask?  
  request.form

- What is a cookie and what kinds of things are they commonly used for?  
  Cookies are name/string-value pair stored by the browser.  They are a way to store small bits of info.

- What is the session object in Flask?  
  Like cookies, you can store information. The info is stored in the browser and is "signed" so users cannot modify the data

- What does Flask's `jsonify()` do?  
  Turns the data into JSON text.  Allows you to create your owen API or use that JSON in JS


  