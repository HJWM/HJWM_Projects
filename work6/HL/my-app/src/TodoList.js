import React, { Component } from 'react';
import './App.css';

class TodoList extends Component {

  constructor(props){
    super(props);
    this.state = {
      list: [
        'Learn English',
        'Learn Chinese',
        'Learn vue'
      ]
    }
  }

  handleBtnClick() {
    this.setState({
      list: [...this.state.list, 'Hello World']
    })
  }

  render() {
    //jsx语法
    return (
      <div>
        <div>
          <input />
          <button onClick={this.handleBtnClick.bind(this)}>add</button>
        </div>
        <div>
          <ul>
            {
              this.state.list.map((item, index) => {
                return <li key={index}>{item}</li>
              })
            }
          </ul>
        </div>
      </div>
    );
  }
}

export default TodoList;
