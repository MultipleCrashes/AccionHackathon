import React from "react";
import ReactDOM from "react-dom";
import Request from "superagent";



class Layout extends React.Component {

	constructor(){
		super();
		this.state = {};
	}

	componentWillMount(){
		var url = "https://api.github.com/repos/vmg/redcarpet/issues?state=closed"
		Request.get(url).then((response) => {
		console.log(response.body);
			this.setState({
				res:response.body
			})
		});
		 

}


 render()
	{
	return <div id="root">
			<h1> Hello Bhai</h1>
			<div id="child">  {JSON.stringify(this.state.res)}</div>
			</div>
	}
}


ReactDOM.render(<Layout/>, document.getElementById('root'))
