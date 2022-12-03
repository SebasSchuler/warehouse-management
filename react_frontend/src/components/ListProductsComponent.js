import React, { Component } from "react";
import { render } from "react-dom";

class ListProductsComponent extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
    };
  }

  componentDidMount() {
    fetch("manager/products")
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
        {this.state.data.map(products => {
          return (
            <div>
                Product name: {products.name} <br/>
                Product Description: {products.description}
            </div>
          );
        })}
      </div>
    );
  }
}

export default ListProductsComponent;

const container = document.getElementById("api");
render(<ListProductsComponent />, container);