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

class ListProductsComponent extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      orders: [],
      warehouses: [],
    };
  }
    handleSubmit = (e) => {
        e.preventDefault();
        console.log("submitted");
        const name = e.target.name.value;
        const description = e.target.description.value;
        const price = e.target.price.value;
        const order = e.target.order.value;
        const warehouse = e.target.warehouse.value;
        const id = e.target.id.value;
        const url = "http://localhost:8000/manager/product/update/".concat(id)
        fetch(url, {
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
          price:price,
          order_id:order,
          warehouse_id:warehouse
          })
        }).then((response) => {
          console.log(response);
          return response.json();
        });
        alert("¡Has actualizado un producto correctamente!");
      };
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

    fetch("manager/orders")
      .then(response => {
        return response.json();
      })
      .then(orders => {
        this.setState(() => {
          return {
            orders,
            loaded: true
          };
        });
      });

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
        {this.state.data.map(products => {
          return (
            <div>
            <br />
            <form onSubmit={this.handleSubmit}>
                Product id: <input type="text" name="id" defaultValue={products.id}/> <br/><br />
                Product name: <input type="text" name="name" defaultValue={products.name}/> <br/><br />
                Product Description: <input type="text" name="description" defaultValue={products.description}/> <br/><br />
                Product Price: <input type="text" name="price" defaultValue={products.price}/> <br/><br />
                Product Order: <select name="order">
                                <option value={products.order_id} selected>{products.order_id}</option>
                                {this.state.orders.map(order => {
                                    return (<option value={order.id}>{order.id}</option>)})}
                                </select>
                <br/><br />
                Product Warehouse: <select name="warehouse">
                                <option value={products.warehouse_id} selected>{products.warehouse_id}</option>
                                {this.state.warehouses.map(warehouse => {
                                    return (<option value={warehouse.id}>{warehouse.id}</option>)})}
                                </select>
                <br /><br />
                <input type="submit" value="Actualizar"/>
            </form>
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