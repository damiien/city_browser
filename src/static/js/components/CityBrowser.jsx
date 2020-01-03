import React, { Component } from 'react';

export default class CityBrowser extends Component {

	constructor() {
		super();
		this.state = { continents : [], countries: [], cities: []};
		this.onSelectContinent = this.onSelectContinent.bind(this);
		this.onSelectCountry = this.onSelectCountry.bind(this);
	}
	
	componentDidMount() {
		fetch("http://localhost:8000/api/continents").then((response) => {
		  return response.json();
		}).then(data => {
		  let list = data.map(cont => { return {value: cont, display: cont} })
		  this.setState({ continents: list });
		  this.loadCountries(list[0].value);
		}).catch(error => {
		  console.log(error);
		});
	}
	
	onSelectContinent(event){
		let continent = event.target.value;
        this.loadCountries(continent);
    }
	
	onSelectCountry(event) {
		let country = event.target.value;
        this.loadCities(country);
	}
	
	loadCountries(continent) {
		fetch("http://localhost:8000/api/countries/continent/" + continent).then((response) => {
		  return response.json();
		}).then(data => {
		  let list = data.map(country => { return {value: country.code, display: country.name} })
		  this.setState({ countries: list });
		  this.loadCities(list[0].value);
		}).catch(error => {
		  console.log(error);
		});
	}
	
	loadCities(country) {
		fetch("http://localhost:8000/api/cities/country/" + country).then((response) => {
		  return response.json();
		}).then(data => {
		  this.setState({ cities: data });
		}).catch(error => {
		  console.log(error);
		});
	}
	 
	render() {
		return (
			<div>
				<label>Select Continent:</label>
				<select onChange={this.onSelectContinent}>
					{this.state.continents.map((cont) => <option key={cont.value} value={cont.value}>{cont.display}</option>)}
				</select>
				<br/>
				<label>Select Country:</label>
				<select onChange={this.onSelectCountry}>
					{this.state.countries.map((cont) => <option key={cont.value} value={cont.value}>{cont.display}</option>)}
				</select>
				<br/>
				<ul>
				{this.state.cities.map((city) => <li>{city.name}</li>)}
				</ul>
			</div>
		)
	}
}