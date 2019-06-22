import React, {Component} from 'react';
import styled from 'styled-components';

const Button = styled.button`
  font-size: 1.5em;
  background-color: grey;
  color: green;
`

class AddItems extends Component {
	
	addFood1() {fetch('https://tfbenvwogg.execute-api.us-east-1.amazonaws.com/stage1/addfood1')}
	addFood2() {fetch('https://tfbenvwogg.execute-api.us-east-1.amazonaws.com/stage1/addfood2')}
	addToy1()  {fetch('https://tfbenvwogg.execute-api.us-east-1.amazonaws.com/stage1/addtoy1')}
	addToy2()  {fetch('https://tfbenvwogg.execute-api.us-east-1.amazonaws.com/stage1/addtoy2')}
	addToy3()  {fetch('https://tfbenvwogg.execute-api.us-east-1.amazonaws.com/stage1/addtoy3')}

	render(){
		return(
			<div className="additemsbox">
				<Button onClick={this.addFood1}> buy kibble </Button>
				<Button onClick={this.addFood2}> buy wet food </Button>
				<Button onClick={this.addToy1}> buy log </Button>
				<Button onClick={this.addToy2}> buy skratcy post </Button>
				<Button onClick={this.addToy3}> buy snugle bed </Button>
			</div>
		);
	}
}

export default AddItems;


//inside the render is a return