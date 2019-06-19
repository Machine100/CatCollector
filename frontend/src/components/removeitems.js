import React, {Component} from 'react';
import styled from 'styled-components';

const Button = styled.button`
  font-size: 1.5em;
  background-color: grey;
  color: red;
`

class RemoveItems extends Component {

	removeFood1() {fetch('https://tfbenvwogg.execute-api.us-east-1.amazonaws.com/stage1/removefood1')}
	removeFood2() {fetch('https://tfbenvwogg.execute-api.us-east-1.amazonaws.com/stage1/removefood2')}
	removeToy1()  {fetch('https://tfbenvwogg.execute-api.us-east-1.amazonaws.com/stage1/removetoy1')}
	removeToy2()  {fetch('https://tfbenvwogg.execute-api.us-east-1.amazonaws.com/stage1/removetoy2')}
	removeToy3()  {fetch('https://tfbenvwogg.execute-api.us-east-1.amazonaws.com/stage1/removetoy3')}

	render(){
		return(
			<div className="removeitemsbox">
				<Button onClick={this.removeFood1}> sell kibble </Button>
				<Button onClick={this.removeFood2}> sell wetfood </Button>
				<Button onClick={this.removeToy1}> sell log </Button>
				<Button onClick={this.removeToy2}> sell skratcy post </Button>
				<Button onClick={this.removeToy3}> sell snugle bed </Button>
			</div>
		);
	}
}

export default RemoveItems;