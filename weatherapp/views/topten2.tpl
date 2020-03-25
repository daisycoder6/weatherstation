<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">

    <!--Import Google Icon Font-->
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <!--Import materialize.css-->
    <link type="text/css" rel="stylesheet" href="/static/css/materialize.min.css" media="screen,projection" />

    <!--Let browser know website is optimized for mobile-->
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

    <title> Temp Sensors </title>
   
  </head>

  <h1 class="center-align red-text"> Recent Temperatures</h1>
  <body>
    %#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)

    <table border="1">

      <thead>
        <tr>
          <th>Record</th>
          <th>Sensor ID</th>
          <th>Timestamp</th>
          <th>Temperature</th>
          <th>Humidity</th>
        </tr>
      </thead>

      </tr>
        %for row in rows:
          <tr>

          %for col in row:
            <td>{{col}}</td>
          %end
          </tr>
        %end
    </table>

    <!--Import jQuery before materialize.js-->
    <script type="text/javascript" src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="/static/js/materialize.min.js"></script>
</body>
</html>