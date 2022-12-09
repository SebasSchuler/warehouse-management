import React, { Component } from "react";
import { render } from "react-dom";
import jQuery from 'jquery'

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
class AddWarehouseComponent extends Component {

  handleSubmit = (e) => {
    e.preventDefault();
    console.log("submitted");
    const body = e.target.address.value;
    fetch("http://localhost:8000/manager/warehouse/create/", {
      method: 'POST',
      headers: {
          'Authorization':'Token ce352f14a56d1430cf78cb6edce20a9fab009fd0',
          'Accept': 'application/json, text/plain, */*',
          'Content-Type': 'application/json',
          'X-CSRFToken': getCookie("csrftoken")
      },
      body: JSON.stringify({address:body})
    }).then((response) => {
      console.log(response);
      return response.json();
    });
  };

  render() {
    return (
      <div>
        <form onSubmit={this.handleSubmit}>
          <label>Address: </label>
          <br />
          <input type="text" name="address" />
          <br />
          <input type="submit" />
        </form>
      </div>
    );
  }
}

const container = document.getElementById("api");
render(<AddWarehouseComponent />, container);