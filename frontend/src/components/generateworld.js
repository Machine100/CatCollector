import React, {Component} from 'react';
import styled from 'styled-components';

const Button = styled.button`

  font-size: 1.5em;
  background-color: darkgrey;
  color: gold;
  padding: 15px;
`


class GenerateWorld extends Component {

	generateWorld() {
		fetch('https://tfbenvwogg.execute-api.us-east-1.amazonaws.com/stage1/generateworld')}

	render(){
		return(
			<div className="delivertoys">
				<Button onClick={this.generateWorld}> Deliver food and toys to the cats. </Button>
			</div>
		);
	}
}

export default GenerateWorld;
