import React, { useState, useEffect } from 'react';
import {
  Layout,
  Typography,
  Table,
  Button,
  Input,
  Select,
  Space,
  message,
  Card,
  Tag,
  Modal,
  Progress,
  Drawer
} from 'antd';
import {
  PlusOutlined,
  DeleteOutlined,
  PlayCircleOutlined,
  CheckCircleOutlined,
  ExclamationCircleOutlined,
  DownloadOutlined,
  FileSearchOutlined
} from '@ant-design/icons';
import axios from 'axios';
import './App.css';

const { Header, Content } = Layout;
const { Title, Text } = Typography;
const { Option } = Select;

function App() {
  const [dataSource, setDataSource] = useState([
    {
      key: 0,
      ref_server: 'Staging',
      curr_server: 'Staging',
      model_name_ref: '',
      model_name_curr: '',
      country_ref: '',
      country_curr: '',
      infolink_ver_ref: '',
      infolink_ver_curr: ''
    }
  ]);
  const [modelNames, setModelNames] = useState([]);
  const [infolinkServers, setInfoLinkServers] = useState([]);
  const [countries, setCountries] = useState([]);
  const [loading, setLoading] = useState(false);
  const [progress, setProgress] = useState(0);
  const [resultsData, setResultsData] = useState(null);
  const [resultsColumns, setResultsColumns] = useState([]);
  const [statistics, setStatistics] = useState(null);
  const [dnaAnalysisVisible, setDnaAnalysisVisible] = useState(false);
  const [dnaAnalysisData, setDnaAnalysisData] = useState([]);
  const [comments, setComments] = useState({});

  // Fetch data from API on component mount
  useEffect(() => {
    fetchModelNames();
    fetchInfoLinkServers();
    fetchCountries();
  }, []);

  const fetchModelNames = async () => {
    try {
      const response = await axios.get('/api/model-names');
      if (response.data.success) {
        setModelNames(response.data.model_names);
      } else {
        message.error('Failed to load model names');
      }
    } catch (error) {
      console.error('Error fetching model names:', error);
      message.error('Failed to load model names from database');
    }
  };

  const fetchInfoLinkServers = async () => {
    try {
      const response = await axios.get('/api/infolink-servers');
      if (response.data.success) {
        setInfoLinkServers(response.data.servers);
      } else {
        message.error('Failed to load InfoLink servers');
      }
    } catch (error) {
      console.error('Error fetching InfoLink servers:', error);
      message.error('Failed to load InfoLink servers from database');
    }
  };

  const fetchCountries = async () => {
    try {
      const response = await axios.get('/api/countries');
      if (response.data.success) {
        setCountries(response.data.countries);
      } else {
        message.error('Failed to load countries');
      }
    } catch (error) {
      console.error('Error fetching countries:', error);
      message.error('Failed to load countries from database');
    }
  };

  const handleInputChange = (key, field, value) => {
    const newData = dataSource.map(item => {
      if (item.key === key) {
        return { ...item, [field]: value };
      }
      return item;
    });
    setDataSource(newData);
  };

  const handleAddRow = () => {
    const newRow = {
      key: dataSource.length,
      ref_server: 'Staging',
      curr_server: 'Staging',
      model_name_ref: '',
      model_name_curr: '',
      country_ref: '',
      country_curr: '',
      infolink_ver_ref: '',
      infolink_ver_curr: ''
    };
    setDataSource([...dataSource, newRow]);
    message.success('New row added');
  };

  const handleDeleteRow = (key) => {
    if (dataSource.length === 1) {
      message.warning('At least one row is required');
      return;
    }
    const newData = dataSource.filter(item => item.key !== key);
    setDataSource(newData);
    message.success('Row deleted');
  };

  const validateData = () => {
    for (let row of dataSource) {
      if (!row.model_name_ref || !row.model_name_curr || 
          !row.country_ref || !row.country_curr ||
          !row.infolink_ver_ref || !row.infolink_ver_curr) {
        message.error('Please fill all fields in all rows');
        return false;
      }
    }
    return true;
  };

  const handleRunAutomation = async () => {
    if (!validateData()) {
      return;
    }

    Modal.confirm({
      title: 'Run Automation',
      icon: <ExclamationCircleOutlined />,
      content: `Are you sure you want to run automation for ${dataSource.length} row(s)? This may take several minutes.`,
      okText: 'Yes, Run',
      okType: 'primary',
      cancelText: 'Cancel',
      onOk: async () => {
        setLoading(true);
        setProgress(0);

        try {
          // Transform data to match backend format
          const payload = dataSource.map(row => ({
            Reference_Server: row.ref_server,
            Current_Server: row.curr_server,
            Model_name_reference: row.model_name_ref,
            Model_name_current: row.model_name_curr,
            Country_reference: row.country_ref,
            Country_current: row.country_curr,
            Infolink_version_reference: row.infolink_ver_ref,
            Infolink_version_current: row.infolink_ver_curr
          }));

          // Simulate progress
          const progressInterval = setInterval(() => {
            setProgress(prev => {
              if (prev >= 90) {
                clearInterval(progressInterval);
                return 90;
              }
              return prev + 10;
            });
          }, 3000);

          const response = await axios.post('/api/run-automation', {
            rows: payload
          });

          clearInterval(progressInterval);
          setProgress(100);

          console.log('🔍 RESPONSE:', {
            success: response.data.success,
            hasData: !!response.data.data,
            dataLength: response.data.data?.length,
            hasColumns: !!response.data.columns,
            columnsLength: response.data.columns?.length,
            hasStatistics: !!response.data.statistics,
            fullResponse: response.data
          });

          if (response.data.success) {
            // Store the results data
            setResultsData(response.data.data);
            setResultsColumns(response.data.columns);
            setStatistics(response.data.statistics);
            
            console.log('✅ State set - resultsData length:', response.data.data?.length);
            
            message.success({
              content: '✅ Automation completed successfully!',
              duration: 5
            });
          } else {
            // Show detailed error message
            const errorMsg = response.data.message || 'Automation failed';
            
            Modal.error({
              title: 'Automation Failed',
              content: (
                <div style={{ whiteSpace: 'pre-wrap', maxHeight: '400px', overflow: 'auto' }}>
                  {errorMsg}
                </div>
              ),
              width: 600,
              okText: 'Close'
            });
          }
        } catch (error) {
          const errorMsg = error.response?.data?.message || error.message;
          
          Modal.error({
            title: 'Error',
            content: (
              <div style={{ whiteSpace: 'pre-wrap', maxHeight: '400px', overflow: 'auto' }}>
                {errorMsg}
              </div>
            ),
            width: 600,
            okText: 'Close'
          });
        } finally {
          setLoading(false);
          setProgress(0);
        }
      }
    });
  };

  const handleDownloadExcel = async () => {
    try {
      const response = await axios.get('/api/download-excel', {
        responseType: 'blob'
      });
      
      // Create a download link
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', 'master_Excel.xlsx');
      document.body.appendChild(link);
      link.click();
      link.remove();
      
      message.success('Excel file downloaded successfully!');
    } catch (error) {
      console.error('Error downloading Excel:', error);
      message.error('Failed to download Excel file');
    }
  };

  const handleDNAAnalysis = () => {
    // Filter data where State Value is 2.1 or 2.2
    const filteredData = resultsData.filter(row => {
      const stateValue = parseFloat(row['State Value']);
      return stateValue === 2.1 || stateValue === 2.2;
    });
    
    // Add row keys and initialize comments
    const dataWithKeys = filteredData.map((row, index) => ({
      ...row,
      key: index,
      Comment: comments[row['App Name']] || ''
    }));
    
    setDnaAnalysisData(dataWithKeys);
    setDnaAnalysisVisible(true);
  };

  const handleCommentChange = (appName, value) => {
    setComments(prev => ({
      ...prev,
      [appName]: value
    }));
  };

  const handleCloseDNAAnalysis = () => {
    setDnaAnalysisVisible(false);
  };

  const getRowStyle = (record) => {
    const color = record.row_color;
    if (color) {
      return { backgroundColor: color };
    }
    return {};
  };

  const columns = [
    {
      title: '#',
      dataIndex: 'key',
      key: 'index',
      width: 50,
      fixed: 'left',
      render: (text, record, index) => index + 1
    },
    {
      title: 'Ref. Server',
      dataIndex: 'ref_server',
      key: 'ref_server',
      width: 130,
      render: (text, record) => (
        <Select
          value={text}
          onChange={(value) => handleInputChange(record.key, 'ref_server', value)}
          style={{ width: '100%' }}
          disabled={loading}
        >
          <Option value="Staging">Staging</Option>
          <Option value="Production">Production</Option>
        </Select>
      )
    },
    {
      title: 'Curr. Server',
      dataIndex: 'curr_server',
      key: 'curr_server',
      width: 130,
      render: (text, record) => (
        <Select
          value={text}
          onChange={(value) => handleInputChange(record.key, 'curr_server', value)}
          style={{ width: '100%' }}
          disabled={loading}
        >
          <Option value="Staging">Staging</Option>
          <Option value="Production">Production</Option>
        </Select>
      )
    },
    {
      title: 'Model Name Ref.',
      dataIndex: 'model_name_ref',
      key: 'model_name_ref',
      width: 180,
      render: (text, record) => (
        <Select
          value={text}
          onChange={(value) => handleInputChange(record.key, 'model_name_ref', value)}
          placeholder="Select Model"
          style={{ width: '100%' }}
          disabled={loading}
          showSearch
          optionFilterProp="children"
          filterOption={(input, option) =>
            option.children.toLowerCase().indexOf(input.toLowerCase()) >= 0
          }
        >
          {modelNames.map(name => (
            <Option key={name} value={name}>{name}</Option>
          ))}
        </Select>
      )
    },
    {
      title: 'Model Name Curr.',
      dataIndex: 'model_name_curr',
      key: 'model_name_curr',
      width: 180,
      render: (text, record) => (
        <Select
          value={text}
          onChange={(value) => handleInputChange(record.key, 'model_name_curr', value)}
          placeholder="Select Model"
          style={{ width: '100%' }}
          disabled={loading}
          showSearch
          optionFilterProp="children"
          filterOption={(input, option) =>
            option.children.toLowerCase().indexOf(input.toLowerCase()) >= 0
          }
        >
          {modelNames.map(name => (
            <Option key={name} value={name}>{name}</Option>
          ))}
        </Select>
      )
    },
    {
      title: 'Country Ref.',
      dataIndex: 'country_ref',
      key: 'country_ref',
      width: 200,
      render: (text, record) => (
        <Select
          value={text}
          onChange={(value) => handleInputChange(record.key, 'country_ref', value)}
          placeholder="Select Country"
          style={{ width: '100%' }}
          disabled={loading}
          showSearch
          optionFilterProp="children"
          filterOption={(input, option) =>
            option.children.toLowerCase().indexOf(input.toLowerCase()) >= 0
          }
        >
          {countries.map(country => (
            <Option key={country} value={country}>{country}</Option>
          ))}
        </Select>
      )
    },
    {
      title: 'Country Curr.',
      dataIndex: 'country_curr',
      key: 'country_curr',
      width: 200,
      render: (text, record) => (
        <Select
          value={text}
          onChange={(value) => handleInputChange(record.key, 'country_curr', value)}
          placeholder="Select Country"
          style={{ width: '100%' }}
          disabled={loading}
          showSearch
          optionFilterProp="children"
          filterOption={(input, option) =>
            option.children.toLowerCase().indexOf(input.toLowerCase()) >= 0
          }
        >
          {countries.map(country => (
            <Option key={country} value={country}>{country}</Option>
          ))}
        </Select>
      )
    },
    {
      title: 'InfoLink Ver. Ref.',
      dataIndex: 'infolink_ver_ref',
      key: 'infolink_ver_ref',
      width: 220,
      render: (text, record) => (
        <Select
          value={text}
          onChange={(value) => handleInputChange(record.key, 'infolink_ver_ref', value)}
          placeholder="Select InfoLink Server"
          style={{ width: '100%' }}
          disabled={loading}
          showSearch
          optionFilterProp="children"
          filterOption={(input, option) =>
            option.children.toLowerCase().indexOf(input.toLowerCase()) >= 0
          }
        >
          {infolinkServers.map(server => (
            <Option key={server} value={server}>{server}</Option>
          ))}
        </Select>
      )
    },
    {
      title: 'InfoLink Ver. Curr.',
      dataIndex: 'infolink_ver_curr',
      key: 'infolink_ver_curr',
      width: 220,
      render: (text, record) => (
        <Select
          value={text}
          onChange={(value) => handleInputChange(record.key, 'infolink_ver_curr', value)}
          placeholder="Select InfoLink Server"
          style={{ width: '100%' }}
          disabled={loading}
          showSearch
          optionFilterProp="children"
          filterOption={(input, option) =>
            option.children.toLowerCase().indexOf(input.toLowerCase()) >= 0
          }
        >
          {infolinkServers.map(server => (
            <Option key={server} value={server}>{server}</Option>
          ))}
        </Select>
      )
    },
    {
      title: 'Action',
      key: 'action',
      width: 80,
      fixed: 'right',
      render: (_, record) => (
        <Button
          type="text"
          danger
          icon={<DeleteOutlined />}
          onClick={() => handleDeleteRow(record.key)}
          disabled={loading || dataSource.length === 1}
        />
      )
    }
  ];

  return (
    <Layout className="layout">
      <Header className="header">
        <div className="header-content">
          <Title level={2} style={{ margin: 0, color: '#fff' }}>
            🧬 DNA Automation
          </Title>
          <Tag color="green" style={{ fontSize: '14px' }}>
            <CheckCircleOutlined /> Logged in as: Yash
          </Tag>
        </div>
      </Header>
      <Content className="content">
        <Card className="main-card">
          <Space direction="vertical" size="large" style={{ width: '100%' }}>
            <div className="info-section">
              <Text type="secondary">
                Enter comparison data for automation. Select model names from dropdowns. Add multiple rows to process batch comparisons.
              </Text>
            </div>

            {loading && (
              <Card className="progress-card">
                <Space direction="vertical" style={{ width: '100%' }}>
                  <Text strong>Running Automation...</Text>
                  <Progress percent={progress} status="active" />
                  <Text type="secondary">
                    Processing {dataSource.length} comparison(s). This may take several minutes...
                  </Text>
                </Space>
              </Card>
            )}

            <div className="table-container">
              <Table
                dataSource={dataSource}
                columns={columns}
                pagination={false}
                bordered
                scroll={{ x: 1500 }}
                loading={loading}
                size="middle"
              />
            </div>

            <div className="button-group">
              <Button
                type="dashed"
                icon={<PlusOutlined />}
                onClick={handleAddRow}
                size="large"
                disabled={loading}
              >
                Add Row
              </Button>
              <Button
                type="primary"
                icon={<PlayCircleOutlined />}
                onClick={handleRunAutomation}
                size="large"
                loading={loading}
                disabled={loading}
              >
                Run Automation
              </Button>
            </div>
          </Space>
        </Card>

        {/* Results Section */}
        {resultsData && Array.isArray(resultsData) && resultsData.length > 0 ? (
          <Card className="main-card" style={{ marginTop: '20px' }}>
            <Space direction="vertical" size="large" style={{ width: '100%' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <Title level={3}>📊 Automation Results</Title>
                <Button
                  type="primary"
                  icon={<DownloadOutlined />}
                  onClick={handleDownloadExcel}
                  size="large"
                >
                  Download Excel
                </Button>
              </div>

              {/* Statistics */}
              {statistics && (
                <Card size="small" style={{ backgroundColor: '#f0f2f5' }}>
                  <Space size="large" wrap>
                    <div>
                      <Text strong>Total Rows: </Text>
                      <Tag color="blue">{statistics.total_rows}</Tag>
                    </div>
                    <div>
                      <Text strong>Total Columns: </Text>
                      <Tag color="blue">{statistics.total_columns}</Tag>
                    </div>
                    <div>
                      <Text strong>State 0 (Match): </Text>
                      <Tag color="green">{statistics.state_0_count}</Tag>
                    </div>
                    <div>
                      <Text strong>State 1 (Mismatch): </Text>
                      <Tag color="red">{statistics.state_1_count}</Tag>
                    </div>
                    <div>
                      <Text strong>State 2.1 (Partial): </Text>
                      <Tag color="orange">{statistics.state_21_count}</Tag>
                    </div>
                    <div>
                      <Text strong>State 2.2 (Not Found): </Text>
                      <Tag color="volcano">{statistics.state_22_count}</Tag>
                    </div>
                  </Space>
                </Card>
              )}

              {/* Results Table */}
              <div className="table-container">
                <Table
                  dataSource={resultsData}
                  columns={resultsColumns.map(col => ({
                    title: col.split('\n').map((line, i) => (
                      <div key={i} style={{ whiteSpace: 'pre-line', textAlign: 'center' }}>{line}</div>
                    )),
                    dataIndex: col,
                    key: col,
                    width: 150,
                    ellipsis: true,
                    render: (text) => text != null ? String(text) : ''
                  }))}
                  scroll={{ x: 'max-content', y: 600 }}
                  pagination={{
                    defaultPageSize: 50,
                    pageSize: 50,
                    showSizeChanger: true,
                    pageSizeOptions: ['50', '100', '200', '500'],
                    showTotal: (total) => `Total ${total} items`
                  }}
                  bordered
                  size="small"
                  rowKey={(record, index) => index}
                  onRow={(record) => ({
                    style: getRowStyle(record)
                  })}
                />
              </div>

              {/* DNA Analysis Button */}
              <div style={{ marginTop: '20px', textAlign: 'center' }}>
                <Button
                  type="primary"
                  size="large"
                  icon={<FileSearchOutlined />}
                  onClick={handleDNAAnalysis}
                  style={{ 
                    background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
                    border: 'none',
                    height: '50px',
                    fontSize: '16px',
                    fontWeight: 'bold',
                    borderRadius: '8px',
                    boxShadow: '0 4px 15px rgba(102, 126, 234, 0.4)'
                  }}
                >
                  🧬 DNA Analysis
                </Button>
              </div>
            </Space>
          </Card>
        ) : null}

        {/* DNA Analysis Drawer */}
        <Drawer
          title={
            <div style={{ fontSize: '20px', fontWeight: 'bold', color: '#355e3b' }}>
              🧬 DNA Analysis - State Value 2.1 & 2.2
            </div>
          }
          placement="right"
          width="90%"
          onClose={handleCloseDNAAnalysis}
          open={dnaAnalysisVisible}
          bodyStyle={{ padding: '24px' }}
        >
          <Card>
            <Space direction="vertical" size="large" style={{ width: '100%' }}>
              <div>
                <Text strong style={{ fontSize: '16px' }}>
                  Total Rows: <Tag color="orange">{dnaAnalysisData.length}</Tag>
                </Text>
                <Text type="secondary" style={{ marginLeft: '20px' }}>
                  Showing apps with version differences or missing versions
                </Text>
              </div>

              <div className="table-container">
                <Table
                  dataSource={dnaAnalysisData}
                  columns={[
                    ...resultsColumns.map(col => ({
                      title: col.split('\n').map((line, i) => (
                        <div key={i} style={{ whiteSpace: 'pre-line', textAlign: 'center' }}>{line}</div>
                      )),
                      dataIndex: col,
                      key: col,
                      width: 150,
                      ellipsis: true,
                      render: (text) => text != null ? String(text) : ''
                    })),
                    {
                      title: 'Comment',
                      dataIndex: 'Comment',
                      key: 'Comment',
                      width: 250,
                      fixed: 'right',
                      render: (text, record) => (
                        <Input.TextArea
                          value={comments[record['App Name']] || ''}
                          onChange={(e) => handleCommentChange(record['App Name'], e.target.value)}
                          placeholder="Add your comment here..."
                          autoSize={{ minRows: 2, maxRows: 4 }}
                          style={{ width: '100%' }}
                        />
                      )
                    }
                  ]}
                  scroll={{ x: 'max-content', y: 600 }}
                  pagination={{
                    defaultPageSize: 50,
                    showSizeChanger: true,
                    pageSizeOptions: ['25', '50', '100', '200'],
                    showTotal: (total) => `Total ${total} items`
                  }}
                  bordered
                  size="small"
                  rowKey={(record, index) => index}
                  onRow={(record) => ({
                    style: getRowStyle(record)
                  })}
                />
              </div>
            </Space>
          </Card>
        </Drawer>
      </Content>
    </Layout>
  );
}

export default App;
