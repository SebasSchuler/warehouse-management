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
    const body = e.target.id.value;
    const url = "http://localhost:8000/manager/product/delete/".concat(body)
    console.log(url)
    fetch(url, {
      method: 'DELETE',
      headers: {
          'Authorization':'Token 2eaa330cb4803995b8cc3474360ac1905f414743',
          'Accept': 'application/json, text/plain, */*',
          'Content-Type': 'application/json',
          'X-CSRFToken': getCookie("csrftoken")
      }
    }).then((response) => {
      console.log(response);
      return response.json();
    });
  };

  render() {
    return (
      <div>
        <form onSubmit={this.handleSubmit}>
          <label>Id: </label>
          <br />
          <input type="text" name="id" />
          <br />
          <input type="submit" />
        </form>
      </div>
    );
  }
}

const container = document.getElementById("api");
render(<AddWarehouseComponent />, container);