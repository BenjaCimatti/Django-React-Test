import React from 'react';
import axios from 'axios';
import foto from './43.png';

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

export default class RandomNumber extends React.Component {
  state = {
    number: ''
  }

  randomize = () => {
    axios.get('/api/random/?format=json')
      .then(res => {
        const number = res.data;
        this.setState({ number });
      })
  }

  async componentDidMount() {
    axios.get('/api/random/?format=json')
      .then(res => {
        const number = res.data;
        this.setState({ number });
      })
  }

  render() {
    return (
      <div>
        <img src={foto}></img>
        <br></br>
        <h>{this.state.number}</h>
        <br></br>
        <button onClick={this.randomize}>Press Me</button>
      </div>
    )
  }
}