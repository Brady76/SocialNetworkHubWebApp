var ContentDiv = React.createClass({
	
	getInitialState: function(){
		return{
			content: {}
		}
	},

	componentDidMount: function(){
		$.ajax({
			url: "http://localhost:8080/",
			type: "GET",
			crossDomain: true,
			success: function(json){
				console.log('success');
				this.setState({
					content: json
				});
				console.log(json);
			}.bind(this)
		});
	},

	postHandler: function(){
		$.ajax({
			url: "http://localhost:8080/",
			type: "POST",
			success: function(){
				console.log('success');
				this.setState({
					content: "POST succeeded"
				})
			}
		})
	},

	render: function(){
		return(
			<div>
			</div>
		)
	}
});

ReactDOM.render(
	<ContentDiv />,
	document.getElementById("content")
)