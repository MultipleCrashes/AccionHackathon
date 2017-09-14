import React from 'react';
import ReactDOM from 'react-dom';

var WebsiteName = React.createClass({
	render: function(){
		return <div> <h3>Enter the email </h3><input type="text" name="email"/>
			<input type="button" name="submit" value="submit"/></div>;
	}
});

ReactDOM.render(React.createElement(WebsiteName), document.body);
