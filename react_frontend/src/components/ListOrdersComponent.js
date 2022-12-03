import React, { Component } from "react";
import { render } from "react-dom";

class ListOrdersComponent extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
    };
  }

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
                order id: {orders.id} <br/>
                order address: {orders.address}
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