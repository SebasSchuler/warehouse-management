import React, { Component } from "react";
import { render } from "react-dom";
import jQuery from 'jquery';

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

class ListWarehousesComponent extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
    };
  }

  handleSubmit = (e) => {
    e.preventDefault();
    console.log("submitted");
    const address = e.target.address.value;
    const id = e.target.id.value;
    const url = "http://localhost:8000/manager/warehouse/update/".concat(id)
    fetch(url, {
      method: 'POST',
      headers: {
          'Authorization':'Token ce352f14a56d1430cf78cb6edce20a9fab009fd0',
          'Accept': 'application/json, text/plain, */*',
          'Content-Type': 'application/json',
          'X-CSRFToken': getCookie("csrftoken")
      },
      body: JSON.stringify({address:address})
    }).then((response) => {
      console.log(response);
      return response.json();
    });
  };
    componentDidMount() {
        fetch("manager/warehouses")
          .then(response => {
            return response.json();
          })
          .then(data => {
            this.setState(() => {
              return {
                data,
                loaded: true
              };
            });
          });
      }

  render() {
    return (
     <div>
        {this.state.data.map(warehouses => {
          return (
            <div>
            <br />
            <form onSubmit={this.handleSubmit}>
                Warehouse id: <input type="text" name="id" defaultValue={warehouses.id}/> <br/><br />
                Warehouse address: <input type="text" name="address" defaultValue={warehouses.address}/>
                <br /><br /><br />
                <input type="submit" value="Actualizar"/>
            </form>
            <br />

            </div>
          );
        })}
      </div>
    );
  }
}

export default ListWarehousesComponent;

const container = document.getElementById("api");
render(<ListWarehousesComponent />, container);