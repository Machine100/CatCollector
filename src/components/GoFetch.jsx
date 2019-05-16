import React, {Component} from 'react';

class GoFetch extends Component {
	state = {
		count: 0,
		monsterpic: 's3://derffred/outputdestination.png'
	}
	render(){
		const {count} = this.state
		const {monsterpic} = this.state
		return(
			<React.Fragment>
				//<img src={monsterpic} alt='' />
				//<span>{monsterpic}</span>
				<span>{count}</span>
				<button>innertext</button>
			</React.Fragment>
		);
	}
}

export default GoFetch;


//inside the render is a return