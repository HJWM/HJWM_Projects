import React, { Component } from 'react';
import './index.css';
//创建棋子组件
class Square extends Component {
    render() {
        return (
            <button className="square" onClick={() => this.props.onClick()}>
                {this.props.value}
            </button>
        );
    }
}
export default Square;