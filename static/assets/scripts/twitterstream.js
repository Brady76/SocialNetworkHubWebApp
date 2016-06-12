var ContentDiv = React.createClass({
	getInitialState: function(){
		return{
			content: {}
		}
	},

	componentDidMount: function(){
		console.log(this.props.dataInput);
		this.setState({
			content: this.props.dataInput
		})
	},

	render: function(){
		//var contentNodes = this.state.content.statuses.map(function(item){
		//	return( 
		//		<ContentNode text = {item.text} hashtags = {item.entities.hashtags}/>
		//	)
		//});

		return(
			<div></div>
		)
	}
});

var ContentNode = React.createClass({
	render:function(){
		var hashtags = this.props.hashtags.map(function(item){
			return(
				<div>{item.text}</div>
			)
		});

		return(
			<div>{this.props.text}   ,   {hashtags}</div>
		)
	}
})

ReactDOM.render(
	<ContentDiv />,
	document.getElementById("content")
)