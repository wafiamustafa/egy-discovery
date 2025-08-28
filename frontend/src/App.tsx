import React, { useState } from 'react'

type PageKey = 'home' | 'analysis' | 'marketing' | 'accounting'

// Analysis Component
const Analysis: React.FC = () => {
  const [topic, setTopic] = useState('August Performance');
  const [roas, setRoas] = useState(2.1);
  const [ctr, setCtr] = useState(0.03);
  const [output, setOutput] = useState<any>('—');
  const [loading, setLoading] = useState(false);

  async function createInsight() {
    setLoading(true);
    try {
      const response = await fetch('/api/analysis/insights', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ topic, data: { roas, ctr } })
      });
      
      const result = await response.json();
      setOutput(result);
    } catch (error) {
      setOutput({ error: error.message });
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="page-container">
      <h1>Market Insight</h1>
      
      <div className="form-group">
        <label className="form-label">Topic:</label>
        <input
          placeholder="Enter topic"
          value={topic}
          onChange={(e) => setTopic(e.target.value)}
          className="form-input"
        />
      </div>

      <div className="form-group">
        <label className="form-label">ROAS (Return on Ad Spend):</label>
        <input
          placeholder="ROAS value"
          type="number"
          step="0.1"
          value={roas}
          onChange={(e) => setRoas(parseFloat(e.target.value) || 0)}
          className="form-input"
        />
      </div>

      <div className="form-group">
        <label className="form-label">CTR (Click Through Rate):</label>
        <input
          placeholder="CTR value"
          type="number"
          step="0.001"
          value={ctr}
          onChange={(e) => setCtr(parseFloat(e.target.value) || 0)}
          className="form-input"
        />
      </div>

      <button
        onClick={createInsight}
        disabled={loading}
        className="btn btn-primary"
      >
        {loading ? 'Creating...' : 'Create Insight'}
      </button>

      <div className="result-section">
        <h3>Result:</h3>
        <pre className="result-output">
          {JSON.stringify(output, null, 2)}
        </pre>
      </div>
    </main>
  );
};

// Marketing Component
const Marketing: React.FC = () => {
  const [campaignData, setCampaignData] = useState({
    platform: 'meta',
    name: '',
    objective: 'LINK_CLICKS',
    budget_daily: 0,
    start_date: '',
    end_date: ''
  });
  
  const [metricData, setMetricData] = useState({
    campaign_id: '',
    date: new Date().toISOString().slice(0, 10),
    impressions: 0,
    clicks: 0,
    spend: 0,
    conversions: 0,
    revenue: 0
  });
  
  const [output, setOutput] = useState<any>('—');
  const [loading, setLoading] = useState(false);

  async function createCampaign() {
    setLoading(true);
    try {
      const response = await fetch('/api/marketing/campaigns', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(campaignData)
      });
      
      const result = await response.json();
      setOutput(result);
    } catch (error) {
      setOutput({ error: error.message });
    } finally {
      setLoading(false);
    }
  }

  async function createMetric() {
    setLoading(true);
    try {
      const response = await fetch('/api/marketing/metrics', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(metricData)
      });
      
      const result = await response.json();
      setOutput(result);
    } catch (error) {
      setOutput({ error: error.message });
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="page-container marketing-page">
      <h1>Marketing Dashboard</h1>
      
      <div className="marketing-grid">
        {/* Campaign Creation */}
        <div className="marketing-section">
          <h2>Create Campaign</h2>
          <div className="form-group">
            <label className="form-label">Platform:</label>
            <select
              value={campaignData.platform}
              onChange={(e) => setCampaignData({...campaignData, platform: e.target.value})}
              className="form-select"
            >
              <option value="meta">Meta (Facebook/Instagram)</option>
              <option value="google">Google Ads</option>
              <option value="tiktok">TikTok</option>
            </select>
          </div>

          <div className="form-group">
            <label className="form-label">Campaign Name:</label>
            <input
              placeholder="Enter campaign name"
              value={campaignData.name}
              onChange={(e) => setCampaignData({...campaignData, name: e.target.value})}
              className="form-input"
            />
          </div>

          <div className="form-group">
            <label className="form-label">Objective:</label>
            <select
              value={campaignData.objective}
              onChange={(e) => setCampaignData({...campaignData, objective: e.target.value})}
              className="form-select"
            >
              <option value="LINK_CLICKS">Link Clicks</option>
              <option value="CONVERSIONS">Conversions</option>
              <option value="REACH">Reach</option>
              <option value="BRAND_AWARENESS">Brand Awareness</option>
            </select>
          </div>

          <div className="form-group">
            <label className="form-label">Daily Budget:</label>
            <input
              type="number"
              step="0.01"
              placeholder="0.00"
              value={campaignData.budget_daily}
              onChange={(e) => setCampaignData({...campaignData, budget_daily: parseFloat(e.target.value) || 0})}
              className="form-input"
            />
          </div>

          <button
            onClick={createCampaign}
            disabled={loading || !campaignData.name}
            className="btn btn-success"
          >
            {loading ? 'Creating...' : 'Create Campaign'}
          </button>
        </div>

        {/* Metrics Creation */}
        <div className="marketing-section">
          <h2>Add Metrics</h2>
          <div className="form-group">
            <label className="form-label">Campaign ID (optional):</label>
            <input
              type="number"
              placeholder="Campaign ID"
              value={metricData.campaign_id}
              onChange={(e) => setMetricData({...metricData, campaign_id: e.target.value})}
              className="form-input"
            />
          </div>

          <div className="form-group">
            <label className="form-label">Date:</label>
            <input
              type="date"
              value={metricData.date}
              onChange={(e) => setMetricData({...metricData, date: e.target.value})}
              className="form-input"
            />
          </div>

          <div className="form-group">
            <label className="form-label">Impressions:</label>
            <input
              type="number"
              placeholder="0"
              value={metricData.impressions}
              onChange={(e) => setMetricData({...metricData, impressions: parseInt(e.target.value) || 0})}
              className="form-input"
            />
          </div>

          <div className="form-group">
            <label className="form-label">Clicks:</label>
            <input
              type="number"
              placeholder="0"
              value={metricData.clicks}
              onChange={(e) => setMetricData({...metricData, clicks: parseInt(e.target.value) || 0})}
              className="form-input"
            />
          </div>

          <div className="form-group">
            <label className="form-label">Spend:</label>
            <input
              type="number"
              step="0.01"
              placeholder="0.00"
              value={metricData.spend}
              onChange={(e) => setMetricData({...metricData, spend: parseFloat(e.target.value) || 0})}
              className="form-input"
            />
          </div>

          <button
            onClick={createMetric}
            disabled={loading}
            className="btn btn-info"
          >
            {loading ? 'Adding...' : 'Add Metrics'}
          </button>
        </div>
      </div>

      <div className="result-section">
        <h3>Result:</h3>
        <pre className="result-output">
          {JSON.stringify(output, null, 2)}
        </pre>
      </div>
    </main>
  );
};

// Accounting Component
const Accounting: React.FC = () => {
  const [transactionData, setTransactionData] = useState({
    date: new Date().toISOString().slice(0, 10),
    type: 'expense',
    account: '',
    counterparty: '',
    currency: 'USD',
    amount: 0,
    category: '',
    description: ''
  });
  
  const [output, setOutput] = useState<any>('—');
  const [loading, setLoading] = useState(false);

  async function createTransaction() {
    setLoading(true);
    try {
      const response = await fetch('/api/accounting/transactions', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(transactionData)
      });
      
      const result = await response.json();
      setOutput(result);
      
      // Reset form on success
      if (response.ok) {
        setTransactionData({
          date: new Date().toISOString().slice(0, 10),
          type: 'expense',
          account: '',
          counterparty: '',
          currency: 'USD',
          amount: 0,
          category: '',
          description: ''
        });
      }
    } catch (error) {
      setOutput({ error: error.message });
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="page-container">
      <h1>Accounting Dashboard</h1>
      
      <div className="accounting-form">
        <h2>Create Transaction</h2>
        
        <div className="form-row">
          <div className="form-group">
            <label className="form-label">Date:</label>
            <input
              type="date"
              value={transactionData.date}
              onChange={(e) => setTransactionData({...transactionData, date: e.target.value})}
              className="form-input"
            />
          </div>

          <div className="form-group">
            <label className="form-label">Type:</label>
            <select
              value={transactionData.type}
              onChange={(e) => setTransactionData({...transactionData, type: e.target.value})}
              className="form-select"
            >
              <option value="expense">Expense</option>
              <option value="income">Income</option>
              <option value="transfer">Transfer</option>
              <option value="refund">Refund</option>
            </select>
          </div>
        </div>

        <div className="form-group">
          <label className="form-label">Account:</label>
          <select
            value={transactionData.account}
            onChange={(e) => setTransactionData({...transactionData, account: e.target.value})}
            className="form-select"
          >
            <option value="">Select Account</option>
            <option value="ops">Operations</option>
            <option value="marketing">Marketing</option>
            <option value="sales">Sales</option>
            <option value="admin">Administrative</option>
            <option value="bank">Bank Account</option>
            <option value="cash">Cash</option>
          </select>
        </div>

        <div className="form-group">
          <label className="form-label">Counterparty:</label>
          <input
            placeholder="Who is this transaction with?"
            value={transactionData.counterparty}
            onChange={(e) => setTransactionData({...transactionData, counterparty: e.target.value})}
            className="form-input"
          />
        </div>

        <div className="form-row">
          <div className="form-group">
            <label className="form-label">Currency:</label>
            <select
              value={transactionData.currency}
              onChange={(e) => setTransactionData({...transactionData, currency: e.target.value})}
              className="form-select"
            >
              <option value="USD">USD</option>
              <option value="EUR">EUR</option>
              <option value="EGP">EGP</option>
              <option value="GBP">GBP</option>
            </select>
          </div>

          <div className="form-group">
            <label className="form-label">Amount:</label>
            <input
              type="number"
              step="0.01"
              placeholder="0.00"
              value={transactionData.amount}
              onChange={(e) => setTransactionData({...transactionData, amount: parseFloat(e.target.value) || 0})}
              className="form-input"
            />
          </div>
        </div>

        <div className="form-group">
          <label className="form-label">Category:</label>
          <select
            value={transactionData.category}
            onChange={(e) => setTransactionData({...transactionData, category: e.target.value})}
            className="form-select"
          >
            <option value="">Select Category</option>
            <option value="advertising">Advertising</option>
            <option value="travel">Travel</option>
            <option value="meals">Meals & Entertainment</option>
            <option value="office">Office Supplies</option>
            <option value="software">Software & Tools</option>
            <option value="services">Professional Services</option>
            <option value="rent">Rent & Utilities</option>
            <option value="salary">Salary & Wages</option>
            <option value="other">Other</option>
          </select>
        </div>

        <div className="form-group">
          <label className="form-label">Description:</label>
          <textarea
            placeholder="Describe this transaction..."
            value={transactionData.description}
            onChange={(e) => setTransactionData({...transactionData, description: e.target.value})}
            className="form-textarea"
          />
        </div>

        <button
          onClick={createTransaction}
          disabled={loading || !transactionData.account || !transactionData.category || transactionData.amount === 0}
          className="btn btn-success"
        >
          {loading ? 'Creating...' : 'Create Transaction'}
        </button>
      </div>

      <div className="result-section">
        <h3>Result:</h3>
        <pre className="result-output">
          {JSON.stringify(output, null, 2)}
        </pre>
      </div>
    </main>
  );
};

// Main App Component
export default function App() {
  const [currentPage, setCurrentPage] = React.useState<PageKey>('home')

  const renderPage = () => {
    switch (currentPage) {
      case 'analysis':
        return <Analysis />
      case 'marketing':
        return <Marketing />
      case 'accounting':
        return <Accounting />
      default:
        return (
          <div className="home-container">
            <h1>Egy Discovery Dashboard</h1>
            <p>Welcome to the comprehensive business intelligence platform.</p>

            <div className="card-grid">
              <div
                className="dashboard-card analysis-card"
                onClick={() => setCurrentPage('analysis')}
              >
                <h3>Market Analysis</h3>
                <p>Create market insights with ROAS and CTR scoring</p>
              </div>
              <div
                className="dashboard-card marketing-card"
                onClick={() => setCurrentPage('marketing')}
              >
                <h3>Marketing</h3>
                <p>Manage ad campaigns and track performance metrics</p>
              </div>
              <div
                className="dashboard-card accounting-card"
                onClick={() => setCurrentPage('accounting')}
              >
                <h3>Accounting</h3>
                <p>Track financial transactions and manage accounts</p>
              </div>
            </div>
          </div>
        )
    }
  }

  return (
    <div className="App">
      <nav className="navbar">
        <div className="nav-inner">
          <h2 onClick={() => setCurrentPage('home')} className="nav-logo">
            Egy Discovery
          </h2>

          <div className="nav-buttons">
            {(['home', 'analysis', 'marketing', 'accounting'] as PageKey[]).map((p) => (
              <button
                key={p}
                onClick={() => setCurrentPage(p)}
                className={`nav-button ${currentPage === p ? 'active' : ''}`}
              >
                {p.charAt(0).toUpperCase() + p.slice(1)}
              </button>
            ))}
          </div>
        </div>
      </nav>

      {renderPage()}
    </div>
  )
}
