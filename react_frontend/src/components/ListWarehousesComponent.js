import React, { Component } from "react";
import { render } from "react-dom";

class ListWarehousesComponent extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
    };
  }

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
                Warehouse id: {warehouses.id} <br/>
                Warehouse address: {warehouses.address}
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