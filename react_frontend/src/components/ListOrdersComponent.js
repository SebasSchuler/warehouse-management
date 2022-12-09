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

class ListOrdersComponent extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
    };
  }
    handleSubmit = (e) => {
        e.preventDefault();
        console.log("submitted");
        const email = e.target.email.value;
        const id = e.target.id.value;
        const url = "http://localhost:8000/manager/order/update/".concat(id)
        fetch(url, {
          method: 'POST',
          headers: {
              'Authorization':'Token ce352f14a56d1430cf78cb6edce20a9fab009fd0',
              'Accept': 'application/json, text/plain, */*',
              'Content-Type': 'application/json',
              'X-CSRFToken': getCookie("csrftoken")
          },
          body: JSON.stringify({
          email:email
          })
        }).then((response) => {
          console.log(response);
          return response.json();
        });
        alert("¡Has actualizado un pedido correctamente!");
      };
  componentDidMount() {
    fetch("manager/orders")
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
        {this.state.data.map(orders => {
          return (
            <div>
            <form onSubmit={this.handleSubmit}>
                Order id: <input type="text" name="id" value={orders.id}/> <br/><br />
                Order email: <input type="text" name="email" defaultValue={orders.email}/> <br/><br />
                <input type="submit" value="Actualizar"/>
                <br/><br/><br/>
            </form>
            </div>
          );
        })}
      </div>
    );
  }
}

export default ListOrdersComponent;

const container = document.getElementById("api");
render(<ListOrdersComponent />, container);