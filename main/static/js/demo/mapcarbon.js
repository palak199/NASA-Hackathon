
  google.charts.load("current", { packages: ["geochart", "corechart"]});
  google.charts.setOnLoadCallback(drawRegionsMapCarbon);
  google.charts.setOnLoadCallback(drawChart);

  function drawRegionsMapCarbon() {
    var data = google.visualization.arrayToDataTable([
      ["Country", "carbon emission"],
      ["Afghanistan", 0.3],
      ["Albania", 1.6],
      ["Algeria", 3.9],
      ["American Samoa", 0.0],
      ["Andorra", 6.0],
      ["Angola", 1.0],
      ["Antigua and Barbuda", 6.2],
      ["Argentina", 4.7],
      ["Armenia", 2.0],
      ["Aruba", 9.3],
      ["Australia", 16.8],
      ["Austria", 8.2],
      ["Azerbaijan", 3.5],
      ["Bahamas", 7.7],
      ["Bahrain", 21.8],
      ["Bangladesh", 0.6],
      ["Barbados", 11.6],
      ["Belarus", 6.8],
      ["Belgium", 9.2],
      ["Belize", 1.2],
      ["Benin", 0.7],
      ["Bermuda", 7.2],
      ["Bhutan", 1.9],
      ["Bolivia", 2.0],
      ["Bosnia and Herzegovina", 7.8],
      ["Botswana", 3.2],
      ["Brazil", 2.4],
      ["British Virgin Islands", 4.8],
      ["Brunei", 16.0],
      ["Bulgaria", 6.3],
      ["Burkina Faso", 0.2],
      ["Burundi", 0.0],
      ["Cape Verde", 1.9],
      ["Cambodia", 0.7],
      ["Cameroon", 0.6],
      ["Canada", 16.1],
      ["Cayman Islands", 8.1],
      ["Central African Republic", 0.1],
      ["Chad", 0.0],
      ["Chile", 5.0],
      ["China", 8.0],
      ["Colombia", 1.8],
      ["Comoros", 0.3],
      ["Democratic Republic of the Congo", 0.0],
      ["Republic of the Congo", 1.3],
      ["Cook Islands", 2.4],
      ["Costa Rica", 1.8],
      ["Ivory Coast", 0.6],
      ["Croatia", 4.7],
      ["Cuba", 2.4],
      ["Curaçao", 52.1],
      ["Cyprus", 6.3],
      ["Czech Republic", 10.4],
      ["Denmark", 5.8],
      ["Djibouti", 1.1],
      ["Dominica", 1.7],
      ["Dominican Republic", 2.3],
      ["Ecuador", 2.6],
      ["Egypt", 2.5],
      ["El Salvador", 1.2],
      ["Equatorial Guinea", 2.5],
      ["Eritrea", 0.2],
      ["Estonia", 18.6],
      ["Eswatini", 0.9],
      ["Ethiopia", 0.2],
      ["Falkland Islands", 13.6],
      ["Faroe Islands", 0.0],
      ["Fiji", 1.4],
      ["Finland", 8.8],
      ["France", 5.0],
      ["French Guiana", 2.6],
      ["French Polynesia", 2.0],
      ["Gabon", 3.2],
      ["Gambia", 0.3],
      ["Georgia", 2.8],
      ["Germany", 9.1],
      ["Ghana", 0.7],
      ["Gibraltar", 19.6],
      ["Greece", 6.5],
      ["Greenland", 9.4],
      ["Grenada", 2.7],
      ["Guadeloupe", 5.2],
      ["Guam", 0.1],
      ["Guatemala", 1.2],
      ["Guinea", 0.2],
      ["Guinea-Bissau", 0.2],
      ["Guyana", 2.5],
      ["Haiti", 0.3],
      ["Honduras", 1.1],
      ["Hong Kong", 6.1],
      ["Hungary", 5.4],
      ["Iceland", 12.1],
      ["India", 1.9],
      ["Indonesia", 2.1],
      ["Iran", 8.9],
      ["Iraq", 4.8],
      ["Ireland", 7.7],
      ["Isle of Man", 0.0],
      ["Israel", 7.9],


    ],);

    var options = {
      colorAxis: {
        colors: [
          "#333333",
          "#112222",
          "#696969",
          "#808080",
          "#020403",
          "#4a4b46",
          "#343434",
          "#0d0c0a",
          "#3b3c36",
          "#777672",
        ],
      },
      legend: "none",
    };

    var chart = new google.visualization.GeoChart(
      document.getElementById("regions_div_carbon")
    );
    chart.draw(data, options);
  }
 


//   this is for water graph
google.charts.setOnLoadCallback(drawRegionsMapWater);
google.charts.setOnLoadCallback(drawChart);
  function drawRegionsMapWater() {
    var data = google.visualization.arrayToDataTable([
      ["Country", "Customer Count", "Agent Count"],
      ["Argentina", 999000, 100],
      ["Australia", 969000, 450],
      ["Belgium", 12000, 200],
      ["Brazil", 850000, 250],
      ["Canada", 1110000, 590],
      ["China", 3975000, 690],
      ["Colombia", 4500, 100],
      ["Denmark", 78600, 150],
      ["France", 67000, 400],
      ["Germany", 140000, 550],
      ["India", 1060000, 560],
      ["Japan", 60000, 420],
      ["Nigeria", 1054000, 305],
      ["Philippines", 120000, 230],
      ["Russia", 2904000, 180],
      ["Singapore", 79000, 450],
      ["South Korea", 15000, 290],
      ["Switzerland", 35000, 230],
      ["United Kingdom", 4015000, 750],
      ["United States", 5000500, 1500],
    ]);

    var options = {
      colorAxis: {
        colors: [
          "#C6E2FF",
          "#0099CC",
          "#60AFFE",
          "#39B7CD",
          "#8EE5EE",
          "#00CDCD",
          "#8FD8D8",
          "#66CCCC",
          "#96CDCD",
        ],
      },
      legend: "none",
    };

    var chart2 = new google.visualization.GeoChart(
      document.getElementById("regions_div_water")
    );
    chart2.draw(data, options);
  }

  $(document).ready(function () {
    $(window).resize(function () {
        drawRegionsMapCarbon();
        drawRegionsMapWater();
        drawRegionsMapWaste();
      
    });
  });
