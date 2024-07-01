import React, {useState, useEffect} from 'react';
import axios from 'axios';
import {Calendar, momentLocalizer} from 'react-big-calendar';
import moment from 'moment';
import 'react-big-calendar/lib/css/react-big-calendar.css'


const localizer = momentLocalizer(moment);

const EventCalendar = () => {
    const [events, setEvents] = useState([]);
    const [newEvent, setNewEvent] = useState({
        title: '',
        description: '',
        start_date: '',
        end_date: ''
    });

    useEffect(() => {
        axios.get('http://127.0.0.1:8000/api/events/')
        .then(respose => {
            setEvents(respose.data)
        })
    }, []);

    const handleInputChange = (e) => {
        const {name, value} = e.target;
        setNewEvent({
            ...newEvent,
            [name]: value,
        });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        const event = {
            ...newEvent,
        };
        axios.post('http://127.0.0.1:8000/api/events/', event)
        .then(respose => {
            setEvents([...events, {
                ...respose.data, 
                start_date: new Date(respose.data.start_date),
                end_date: new Date(respose.data.end_date),
            }]);
            setNewEvent({
                title: '',
                description: '',
                start_date: '',
                end_date: ''
            });
        });
    };

    return(
        <div>
            <h1>Event Calendar</h1>
            <Calendar
                localizer={localizer}
                events={events}
                startAccessor="start_date"
                endAccessor="end_date"
                style={{ height: 500 }}
            />
            <form onSubmit={handleSubmit}>
                <input 
                    type='text' 
                    name='title' 
                    placeholder='Title' 
                    value={newEvent.title} 
                    onChange={handleInputChange} 
                />
                <input 
                    type='text' 
                    name='description' 
                    placeholder='Description' 
                    value={newEvent.description} 
                    onChange={handleInputChange} 
                />
                <input 
                    type='datetime-local' 
                    name='start_date' 
                    value={newEvent.start_date} 
                    onChange={handleInputChange} 
                />
                <input 
                    type='datetime-local' 
                    name='end_date' 
                    value={newEvent.end_date} 
                    onChange={handleInputChange} 
                />
                <button type='submit'>Add new event</button>
            </form>
        </div>
    );
}

export default EventCalendar;