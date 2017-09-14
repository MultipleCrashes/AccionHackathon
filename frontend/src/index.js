import React from 'react';
import ReactDOM from 'react-dom';

var WebsiteName = React.createClass({
	render: function(){
		return <div> Welcome to Web!! </div>;
	}
});

ReactDOM.render(React.createElement(WebsiteName), document.body);
