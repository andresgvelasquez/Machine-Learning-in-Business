import React, { useState, useEffect } from 'react';
import axios from 'axios';

function CorrelationMatrix() {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:8000/portfolio/api/correlation-matrix/');
                console.log(response.data);
                setData(response.data);
                setLoading(false);
            } catch (error) {
                console.error('Error fetching data:', error);
                setError(`Error fetching data: ${error.message}`);
                setLoading(false);
            }
        };

        fetchData();
    }, []);

    if (loading) return <div>Loading...</div>;
    if (error) return <div>{error}</div>;

    return (
        <div>
            <h2>Correlation Matrix</h2>
            <pre>{JSON.stringify(data, null, 2)}</pre>
        </div>
    );
}

export default CorrelationMatrix;