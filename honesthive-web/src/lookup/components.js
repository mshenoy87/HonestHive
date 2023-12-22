function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
  
export function backendLookup(method, endpoint, callback, data) {
    let jsonData;
    if (data) {
      jsonData = JSON.stringify(data);
    }
    const xmlRequest = new XMLHttpRequest();
    const url = `http://localhost:8000/api${endpoint}`;
    // get information from backend
    xmlRequest.responseType = "json";
    xmlRequest.open(method, url);
    
    let csrftoken = getCookie('csrftoken');
    xmlRequest.setRequestHeader("Content-Type", "application/json");

    if (csrftoken) {
      xmlRequest.setRequestHeader("X-Requested-With", "XMLHttpRequest");
      xmlRequest.setRequestHeader("X-CSRFToken", csrftoken);
    }

    xmlRequest.onload = function() {
      if (xmlRequest.status === 403) {
        const detail = xmlRequest.response.detail;
        if (detail === "Authentication credentials were not provided.") {
          if (window.location.href.indexOf("login") === -1) {
            window.location.href = "/login?showLoginRequired=true";
          }
        }
      }

      callback(xmlRequest.response, xmlRequest.status);
  
    }
    xmlRequest.onerror = function(e) {
      callback({"message": "The request returned an error"}, 400);
    }

    xmlRequest.send(jsonData);
  
}