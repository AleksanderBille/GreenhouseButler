var gridColor = "rgba(107, 0, 60, 1)"
var noColor = "rgba(0, 0, 0, 0)"
var actuatorColor = "rgba(0, 255, 0, 1)"
var watchdogColor = "rgba(255, 0, 0, 1)"
var backgroundColor = "rgba(0,0,0,0)"
var hoverBackgroundColor = "rgba(107, 0, 60, 1)"
var hoverBorderColor = "rgba(107, 0, 60, 1)"
var borderColor = "rgba(107, 0, 60, 1)"


//Get data from file, and put into arrays
async function readLog(file,labelArr,dataArr, colorArr) {
fetch(file).then((file) => file.text()
).then(text => {
  var data = text.split(/\s+/);
  for (var i = 0; i < data.length; i++) {
    if (i % 7 == 2) { //Get time of day
      labelArr.push(data[i]);
    }
    else if (i % 7 == 3) { // Get data
      dataArr.push(Number(data[i]));
    }
    else if (i % 7 == 4){
      if(data[i] == '1') {           //Check for WatchDog flag
        colorArr.push(watchdogColor);
      } else if (data[i+1] == '1') {//Check for Actuator flag
        colorArr.push(actuatorColor);
      } else {                      //No flags
        colorArr.push(noColor);  
      }
    }
  }
});
}

var JordfugtLabels = [];
var JordfugtData = [];
var JordfugtColor = [];

await readLog("Jordfugt.txt", JordfugtLabels, JordfugtData, JordfugtColor);


var data1 = {
  labels: JordfugtLabels,
  datasets: [{
    label: "Jordfugtighed",
    backgroundColor: backgroundColor,
    borderColor: JordfugtColor,
    borderWidth: 2,
    pointBackgroundColor: JordfugtColor,
    hoverBackgroundColor: hoverBackgroundColor,
    hoverBorderColor: hoverBorderColor,
    data: JordfugtData,
  }]
};



var options1 = {
  maintainAspectRatio: false,
  responsive: true,
  scales: {
    yAxes: [{
      stacked: true,
      gridLines: {
        display: true,
        color: gridColor
      }
    }],
    xAxes: [{
      gridLines: {
        display: false
      }
    }]
  }
};

setTimeout(
  function () {
    Chart.Line('chart-1', {
      options: options1,
      data: data1
    }
    )
  }, 500
);

var LuftfugtLabels = [];
var LuftfugtData = [];
var LuftfugtColor = [];
await readLog("Luftfugt.txt",LuftfugtLabels,LuftfugtData, LuftfugtColor);

var data2 = {
  labels: LuftfugtLabels,
  datasets: [{
    label: "Luftfugtighed",
    backgroundColor: backgroundColor,
    borderColor: LuftfugtColor,
    borderWidth: 2,
    pointBackgroundColor: LuftfugtColor,
    hoverBackgroundColor: hoverBackgroundColor,
    hoverBorderColor: hoverBorderColor,
    data: LuftfugtData,
  }]
};



var options2 = {
  maintainAspectRatio: false,
  responsive: true,
  scales: {
    yAxes: [{
      stacked: true,
      gridLines: {
        display: true,
        color: gridColor
      }
    }],
    xAxes: [{
      gridLines: {
        display: false
      }
    }]
  }
};

setTimeout(
  function () {
    Chart.Line('chart-2', {
      options: options2,
      data: data2
    }
    )
  }, 500
);


var TemperaturLabels = [];
var TemperaturData = [];
var TemperaturColor = [];

await readLog("Temperatur.txt", TemperaturLabels, TemperaturData, TemperaturColor);

var data3 = {
  labels: TemperaturLabels,
  datasets: [{
    label: "Temperatur",
    backgroundColor: backgroundColor,
    borderColor: TemperaturColor,
    borderWidth: 2,
    pointBackgroundColor: TemperaturColor,
    hoverBackgroundColor: hoverBackgroundColor,
    hoverBorderColor: hoverBorderColor,
    data: TemperaturData,
  }]
};

var options3 = {
  maintainAspectRatio: false,
  responsive: true,
  scales: {
    yAxes: [{
      stacked: true,
      gridLines: {
        display: true,
        color: gridColor
      }
    }],
    xAxes: [{
      gridLines: {
        display: false
      }
    }]
  }
};

setTimeout(
  function () {
    Chart.Line('chart-3', {
      options: options3,
      data: data3
    }
    )
  }, 500
);


var SollysLabels = [];
var SollysData = [];
var SollysColor = [];

await readLog("Sollys.txt", SollysLabels, SollysData, SollysColor);

var data4 = {
  labels: SollysLabels,
  datasets: [{
    label: "Sollys",
    backgroundColor: backgroundColor,
    borderColor: SollysColor,
    borderWidth: 2,
    pointBackgroundColor: SollysColor,
    hoverBackgroundColor: hoverBackgroundColor,
    hoverBorderColor: hoverBorderColor,
    data: SollysData,
  }]
};

var options4 = {
  maintainAspectRatio: false,
  responsive: true,
  scales: {
    yAxes: [{
      stacked: true,
      gridLines: {
        display: true,
        color: gridColor
      }
    }],
    xAxes: [{
      gridLines: {
        display: false
      }
    }]
  }
};

setTimeout(
  function () {
    Chart.Line('chart-4', {
      options: options4,
      data: data4
    }
    )
  }, 500
);
