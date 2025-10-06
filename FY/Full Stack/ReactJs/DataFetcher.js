// src/DataFetcher.js
import React, { Component } from "react";

class DataFetcher extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
    };
  }

  componentDidMount() {
    fetch("https://jsonplaceholder.typicode.com/posts")
      .then((response) => response.json())
      .then((data) => this.setState({ data }));
  }

  render() {
    return (
      <div>
        <h2>Fetched Data</h2>
        <ul>
          {this.state.data.slice(0, 5).map((item) => (
            <li key={item.id}>{item.title}</li>
          ))}
        </ul>
      </div>
    );
  }
}

export default DataFetcher;
