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
class DeleteProductComponent extends Component {
  constructor(props) {
    super(props);
    this.state = {
      products: [],
    };
  }

  handleSubmit = (e) => {
    e.preventDefault();
    console.log("submitted");
    const body = e.target.id.value;
    const url = "http://localhost:8000/manager/product/delete/".concat(body)
    console.log(url)
    fetch(url, {
      method: 'DELETE',
      headers: {
          'Authorization':'Token ce352f14a56d1430cf78cb6edce20a9fab009fd0',
          'Accept': 'application/json, text/plain, */*',
          'Content-Type': 'application/json',
          'X-CSRFToken': getCookie("csrftoken")
      }
    }).then((response) => {
      console.log(response);
      return response.json();
    });
  };
  componentDidMount() {
    fetch("manager/products")
      .then(response => {
        return response.json();
      })
      .then(products => {
        this.setState(() => {
          return {
            products,
            loaded: true
          };
        });
      });
  }

  render() {
    return (
      <div>
        <form onSubmit={this.handleSubmit}>
          <label>Selecciona un producto: </label>
          <br />
          <select name="id">
                                {this.state.products.map(product => {
                                    return (<option value={product.id}>{product.name}</option>)})}
                                </select>
          <br />
          <input type="submit" />
        </form>
      </div>
    );
  }
}

const container = document.getElementById("api");
render(<DeleteProductComponent />, container);