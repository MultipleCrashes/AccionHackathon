import React from 'react';
import ReactDOM from 'react-dom';

var WebsiteName = React.createClass({
	render: function(){
		return <div id="website"> Welcome to Web!! </div>;
	}
});


var BgImageClass = React.createClass({
	render: function(){
		return <div id="welcome"> Hello World </div>;
	}
});

ReactDOM.render(React.createElement(WebsiteName), document.getElementById("website"));
ReactDOM.render(React.createElement(BgImageClass), document.getElementById("welcome"));
