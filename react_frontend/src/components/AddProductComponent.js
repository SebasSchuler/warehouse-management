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
    constructor(props) {
        super(props);
        this.state = {
          warehouses: [],
        };
      }
  handleSubmit = (e) => {
    e.preventDefault();
    console.log("submitted");
    const name = e.target.name.value;
    const description = e.target.description.value;
    const price = e.target.price.value;
    const warehouse = e.target.warehouse.value;
    fetch("http://localhost:8000/manager/product/create/", {
      method: 'POST',
      headers: {
          'Authorization':'Token 2eaa330cb4803995b8cc3474360ac1905f414743',
          'Accept': 'application/json, text/plain, */*',
          'Content-Type': 'application/json',
          'X-CSRFToken': getCookie("csrftoken")
      },
      body: JSON.stringify({
      name:name,
      description:description,
      price: parseFloat(price),
      warehouse_id: warehouse
      })
    }).then((response) => {
      console.log(response);
      return response.json();
    });
    alert("¡Has añadido un producto correctamente!");
  };
  componentDidMount() {
    fetch("manager/warehouses")
      .then(response => {
        return response.json();
      })
      .then(warehouses => {
        this.setState(() => {
          return {
            warehouses,
            loaded: true
          };
        });
      });
  }
  render() {
    return (
      <div>
        <form onSubmit={this.handleSubmit}>
          <label>Name: </label>
          <br />
          <input type="text" name="name" />
          <br />
          <label>Description: </label>
          <br />
          <input type="text" name="description" />
          <br />
          <label>Price: </label>
          <br />
          <input type="text" name="price" />
          <br/>
          <label>Warehouse: </label>
          <br/>
                <select name="warehouse">
                                {this.state.warehouses.map(warehouse => {
                                    return (<option value={warehouse.id}>{warehouse.id}</option>)})}
                                </select>
          <br/><br/>
          <input type="submit" />
        </form>
      </div>
    );
  }
}

const container = document.getElementById("api");
render(<AddWarehouseComponent />, container);