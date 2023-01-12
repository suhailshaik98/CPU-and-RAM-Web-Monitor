
function getyears(){
  let year_start = document.getElementById("year_start");
  let year_start_value = get_value_and_clear(year_start);
  let year_end = document.getElementById("year_end");
  let year_end_value = get_value_and_clear(year_end);
  let dic = {"hour_start": year_start_value,  "hour_end": year_end_value};
  let dicJSON = JSON.stringify(dic);
  ajaxPostRequest("/donut", dicJSON,displaychart)
  ajaxPostRequest("/donut2", dicJSON,displaychart1);

}


function displaychart(response){
    let data = JSON.parse(response);
    let mydiv=document.getElementById("songs");
    let s = data[0]["name"];
    let f = data[data.length-1]["name"];
    let layout = {
      title: 'RAM used by each application',
      showlegend: true,
xaxis: {type: 'date',title: 'Hour'},
  yaxis: {title: 'RAM Average'}
    };
    Plotly.newPlot(mydiv, data, layout);

}
function displaychart1(response){
    let data = JSON.parse(response);
    let mydiv=document.getElementById("songs1");
    let s = data[0]["name"];
    let f = data[data.length-1]["name"];
    let layout = {
      title: 'CPU and RAM Usage',
      showlegend: true,
xaxis: {type: 'date',title: 'Hour'},
  yaxis: {title: 'Usage Percentage'}
    };
    Plotly.newPlot(mydiv, data, layout);

}
function get_value_and_clear(input_obj) {
  let retVal = input_obj.value;
  input_obj.value = "";
  return retVal;
}


function ajaxGetRequest(path, callback){
    let request = new XMLHttpRequest();
    request.onreadystatechange = function(){
        if (this.readyState===4&&this.status ===200){
            callback(this.response);
        }
    };
    request.open("GET", path);
    request.send();
}

// path is URL we are sending request
// data is JSON blob being sent to the server
// callback function that JS calls when server replies
function ajaxPostRequest(path, data, callback){
    let request = new XMLHttpRequest();
    request.onreadystatechange = function(){
        if (this.readyState===4&&this.status ===200){
            callback(this.response);
        }
    };
    request.open("POST", path);
    request.send(data);
}