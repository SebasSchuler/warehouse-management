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
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ title: 'React POST Request Example' })
        };
        fetch('manager/product/create', requestOptions)
            .then(response => response.json())
            .then(data => this.setState({ postId: data.id }));
    }
}