const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const schema = new Schema({
    Header: {
        type: String,
        required: true
    },
    Time: {
        type: String,
    },
    Link: {
        type: String,
        required: true
    },
    Text: {
        type: String,
        required: true
    }
})

module.exports = mongoose.model('New', schema)