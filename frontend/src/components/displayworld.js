import React, {Component} from 'react';

class DisplayWorld extends Component {
	state = {
		worldview: 'https://s3.amazonaws.com/derffred/worldview.png'
	}
	

	generateWorld() {
		fetch('https://tfbenvwogg.execute-api.us-east-1.amazonaws.com/stage1/generateworld')}

	render(){
		const {worldview} = this.state
		return(
			<div className="worldbox">
				<img src={worldview} alt='' />
			</div
			>
		);
	}
}

export default DisplayWorld;


//inside the render is a return